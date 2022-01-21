import airflow
from airflow import DAG
from airflow.models import Variable
from airflow.utils.dates import days_ago
from airflow.providers.amazon.aws.transfers.gcs_to_s3 import GCSToS3Operator


default_args = {
    "start_date": days_ago(0),
}

with DAG(
    "gcs_to_s3",
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
) as dag:

    task_gcs_to_s3 = GCSToS3Operator(
        task_id="gcs_to_s3",
        bucket="{your-gcs-bucket}",
        dest_s3_key="s3://{your-s3-bucket}/",
        replace=True,
    )