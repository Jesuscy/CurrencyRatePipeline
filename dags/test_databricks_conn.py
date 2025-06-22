from airflow import DAG
from airflow.providers.databricks.operators.databricks import DatabricksSubmitRunOperator
from datetime import datetime
import os
from dotenv import load_dotenv

with DAG("test_databricks_conn", start_date=datetime(2024, 1, 1), schedule=None, catchup=False) as dag:

    test_task = DatabricksSubmitRunOperator(
        task_id="test_run",
        databricks_conn_id="databricks_default",
        json={
            "existing_cluster_id": f"{os.getenv('CLUSTER_ID')}",
            "notebook_task": {
                "notebook_path": f"/Users/{os.getenv('MAIL')}/notebooks/01_raw_to_curated"
            }
        },
    )
