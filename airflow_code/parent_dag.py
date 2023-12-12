# Define Parent DAG
from datetime import datetime,timedelta
from time import sleep
from airflow import DAG
from airflow.operators.python_operator import PythonOperator


#Define the sleep function
def sleep_for_180_seconds():
    sleep(180)

# define default arguments for dag
default_args = {
    'owner':'swamini',
    'start_date':datetime(2023,12,11),
    'retries':1,
    'retry_delay':timedelta(minutes=1)
}

# Define the DAG
dag = DAG('parent_dag',default_args = default_args,schedule_interval=timedelta(days=1))

# Task to sleep for 180 seconds
task_to_wait_for = PythonOperator(
    task_id = 'task_to_wait_for',
    python_callable = sleep_for_180_seconds,
    provide_context = True,
    dag = dag,
)


