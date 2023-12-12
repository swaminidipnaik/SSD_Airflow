# Dependent_DAG
from datetime import datetime,timedelta
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.sensors.external_task_sensor import ExternalTaskSensor

# define default arguments for dag
default_args = {
    'owner':'swamini',
    'start_date':datetime(2023,12,11),
    'retries':1,
    'retry_delay':timedelta(minutes=1)
}

# Define the DAG
dag = DAG('dependent_dag',default_args=default_args,schedule_interval=timedelta(days=1))

# starting_task
start_task = DummyOperator(task_id = 'start_task',dag = dag)

# Use ExternalTaskSensor to wait for task_to_wait_for
wait_for_task = ExternalTaskSensor(
    task_id = 'wait_for_task',
    external_dag_id = 'parent_dag',
    external_task_id = 'task_to_wait_for',
    dag = dag,
)

# Task to execute after waiting
dependent_task = DummyOperator(task_id = 'dependent_task',dag = dag)

# Define task dependencies
start_task >> wait_for_task >> dependent_task