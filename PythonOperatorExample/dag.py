from __future__ import annotations

import pendulum

from airflow.models.dag import DAG
from airflow.operators.python import PythonOperator

def print_execution_date(**kwargs):
    print(kwargs["ds"])

with DAG(
    dag_id="python_operator_example",
    start_date=pendulum.datetime(2023, 10, 26, tz="UTC"),
    catchup=False,
    schedule=None,
    tags=["example"],
) as dag:
    run_this = PythonOperator(
        task_id="print_the_context",
        python_callable=print_execution_date,
    )
