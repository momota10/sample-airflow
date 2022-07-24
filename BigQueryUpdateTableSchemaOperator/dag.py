import os
import json
from typing import List
from datetime import datetime
from airflow import DAG
from airflow.providers.google.cloud.operators.bigquery import BigQueryUpdateTableSchemaOperator

DAG_NAME = "update_table_schema"
DAG_HOME_PATH = os.path.abspath(os.path.dirname(__file__))


def read_schema_file(table_name: str) -> List:
    with open(f"{DAG_HOME_PATH}/schema/{table_name}.json", "r") as f:
        df = json.load(f)

    return df


default_args = {
    "start_date": datetime(2015, 1, 23, 0, 0),
}


with DAG(
    DAG_NAME,
    schedule_interval=None,
    catchup=False,
    default_args=default_args,
) as dag:

    task_update_table_schema = BigQueryUpdateTableSchemaOperator(
        task_id="update_table_schema",
        dataset_id="your-dataset",
        table_id="users",
        include_policy_tags=True,
        schema_fields_updates=read_schema_file("users")
    )
