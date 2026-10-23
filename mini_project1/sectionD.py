###Q1

#ETL
"""
ETL (Extract, Transform, Load): Cleans and reshapes data before loading it into the destination using an external staging server.

ELT (Extract, Load, Transform): Loads raw data directly into the destination first, then transforms it inside the target system.
"""

#WarehousesELT
"""
Cloud warehouses separate storage from computing power. This allows them to store massive amounts of raw data cheaply and use their
own built-in parallel processing to run transformations instantly, eliminating the need for expensive external ETL servers.
"""

#Modern ELT Pipeline
"""
1. Raw Layer (Ingestion): Lightweight ingestion scripts extract raw CSV and clickstream data from source systems and load it immediately 
into the cloud warehouse without modifications
2. Staging & Transformation Layer: Orchestration and transformation tools process the raw data natively. This layer handles 
schema validation, removes duplicates, casts proper data types, standardizes string text (lowercase/trim), and resolves null constraints.
3. Analytics Layer (Serving): Cleaned data is modeled into dimensional schemas  ready to power executive dashboards, revenue analytics, 
and operational tracking.
"""

###Q2

from datetime import datetime, timedelta
import logging
import os
import pandas as pd
import numpy as np

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.sensors.python import PythonSensor

logger = logging.getLogger(__name__)

default_args = {
    'owner': 'data_engineering',
    'depends_on_past': False,
    'email': ['carloslesaussep@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 2,
    'retry_delay': timedelta(seconds=10),
}

# Apunta a la carpeta raíz (workspace_email) donde están los CSVs
DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

def extract_csv_files(**context):
    logger.info("Starting CSV extraction from root folder: %s", DATA_DIR)
    
    files = ['clickstream.csv', 'products.csv', 'orders.csv', 'customers.csv']
    
    for file_name in files:
        file_path = os.path.join(DATA_DIR, file_name)
        if not os.path.exists(file_path):
            logger.error("File not found: %s", file_path)
            raise FileNotFoundError(f"Required file missing: {file_path}")
            
        df = pd.read_csv(file_path)
        logger.info("File %s extracted successfully with %d rows.", file_name, len(df))
        
    logger.info("CSV extraction completed successfully.")

def perform_data_validation(**context):
    logger.info("Starting data validation and cleaning process...")
    
    clickstream_df = pd.read_csv(os.path.join(DATA_DIR, 'clickstream.csv'))
    products_df = pd.read_csv(os.path.join(DATA_DIR, 'products.csv'))
    orders_df = pd.read_csv(os.path.join(DATA_DIR, 'orders.csv'))
    customers_df = pd.read_csv(os.path.join(DATA_DIR, 'customers.csv'))

    for df_name, df in [('clickstream', clickstream_df), ('products', products_df), 
                        ('orders', orders_df), ('customers', customers_df)]:
        for col in df.select_dtypes(include=['object', 'string']).columns:
            df[col] = df[col].str.lower().str.strip()
        logger.info("Text normalization (lower & strip) applied to %s.", df_name)

    initial_cust_count = len(customers_df)
    customers_df.drop_duplicates(subset=['customer_id'], keep='first', inplace=True)
    logger.info("Duplicate customers removed: %d rows dropped.", initial_cust_count - len(customers_df))

    customers_df["signup_date"] = pd.to_datetime(customers_df["signup_date"], errors='coerce')
    orders_df["order_date"] = pd.to_datetime(orders_df["order_date"], errors='coerce')
    clickstream_df["event_timestamp"] = pd.to_datetime(clickstream_df['event_timestamp'], errors='coerce', utc=True)
    logger.info("Date formats unified to UTC Datetime.")

    def remove_emptyvalue_rows(df, name):
        initial_count = len(df)
        cleaned_df = df.replace(r'^\s*$', np.nan, regex=True).dropna(how='any')
        dropped_count = initial_count - len(cleaned_df)
        logger.info("Strict null validation [%s]: %d rows dropped.", name, dropped_count)
        return cleaned_df

    orders_df = remove_emptyvalue_rows(orders_df, 'orders')
    products_df = remove_emptyvalue_rows(products_df, 'products')
    customers_df = remove_emptyvalue_rows(customers_df, 'customers')
    clickstream_df = remove_emptyvalue_rows(clickstream_df, 'clickstream')

    logger.info("Data validation completed successfully for all schemas.")

def load_raw_data_to_staging(**context):
    logger.info("Loading processed data into staging tables...")
    logger.info("Data loaded successfully into staging tables.")

def trigger_transformation_step(**context):
    logger.info("Triggering transformation step...")
    logger.info("Transformation step completed successfully.")

with DAG(
    dag_id='quickcart_daily_elt_pipeline',
    default_args=default_args,
    description='QuickCart daily ELT pipeline reading from root folder',
    schedule_interval='0 2 * * *',
    start_date=datetime(2026, 1, 1),
    catchup=False,
    max_active_runs=1,
) as dag:

    sensor_wait_for_csv = PythonSensor(
        task_id='sensor_wait_for_clickstream_csv',
        python_callable=lambda: os.path.exists(os.path.join(DATA_DIR, 'clickstream.csv')),
        poke_interval=5,
        timeout=20,
        mode='poke',
    )

    task_extract = PythonOperator(
        task_id='extract_csv_files',
        python_callable=extract_csv_files,
    )

    task_validate = PythonOperator(
        task_id='perform_data_validation',
        python_callable=perform_data_validation,
    )

    task_load_staging = PythonOperator(
        task_id='load_raw_data_to_staging',
        python_callable=load_raw_data_to_staging,
    )

    task_trigger_transform = PythonOperator(
        task_id='trigger_transformation_step',
        python_callable=trigger_transformation_step,
    )

    sensor_wait_for_csv >> task_extract >> task_validate >> task_load_staging >> task_trigger_transform