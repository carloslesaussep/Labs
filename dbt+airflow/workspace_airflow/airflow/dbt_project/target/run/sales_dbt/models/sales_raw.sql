
    

    create  table
      "warehouse"."main"."sales_raw__dbt_tmp"
  
    
    as (
      

SELECT 
    order_id,
    customer,
    city,
    product,
    quantity,
    price
FROM read_csv_auto(
    '/opt/airflow/data/sales.csv',
    header = true
)
    );
    
  