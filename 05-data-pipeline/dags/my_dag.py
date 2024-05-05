from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.utils import timezone

with DAG(
    "my_dag",
    start_date=timezone.datetime(2024, 5, 5),
    schedule=None,
    tags=["DS525"]
):
    my_task = EmptyOperator(task_id="my_task")
    my_task_II = EmptyOperator(task_id="my_task_II")

    my_task >> my_task_II