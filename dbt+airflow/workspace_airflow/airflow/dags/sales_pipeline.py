from datetime import datetime
from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator

DBT_PROJECT_DIR = "/opt/airflow/dbt_project"
DBT_PROFILES_DIR = "/opt/airflow/dbt_project/profiles"

with DAG(
    dag_id="sales_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule=None,  # Manual por ahora para pruebas
    catchup=False,
    tags=["dbt", "duckdb", "lab"]
) as dag:

    start = EmptyOperator(task_id="start")

    load_csv = BashOperator(
        task_id="load_csv",
        bash_command="echo Loading CSV..."
    )

    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command=f"dbt run --project-dir {DBT_PROJECT_DIR} --profiles-dir {DBT_PROFILES_DIR}"
    )

    dbt_test = BashOperator(
        task_id="dbt_test",
        bash_command=f"dbt test --project-dir {DBT_PROJECT_DIR} --profiles-dir {DBT_PROFILES_DIR}"
    )

    end = EmptyOperator(task_id="end")

    start >> load_csv >> dbt_run >> dbt_test >> end