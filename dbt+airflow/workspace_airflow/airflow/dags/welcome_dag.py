from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id='simple_welcome_dag',
    start_date=datetime(2026, 1, 1),
    schedule='@daily',
    catchup=False,
) as dag:

    say_hello = BashOperator(
        task_id='welcome_and_date',
        bash_command='echo "¡Hola! Bienvenido a tu pipeline. La fecha de ejecución es: {{ ds }}"',
    )