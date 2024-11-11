from datetime import timedelta, datetime

from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.providers.cncf.kubernetes.operators.spark_kubernetes import SparkKubernetesOperator
from airflow.providers.cncf.kubernetes.sensors.spark_kubernetes import SparkKubernetesSensor

default_args = {
    'owner': 'test',
    'start_date': datetime(2024, 1, 1),
    'depends_on_past': True,
    'retries': 0,
    'retry_delay': timedelta(hours=1),
}

with DAG(
        dag_id="trigger-spark-operator",
        default_args=default_args,
        # schedule_interval='0 5 * * *',
        dagrun_timeout=timedelta(days=1),
        description='trigger spark operator',
        catchup=False,
) as dag:

    # start dummy task
    start = DummyOperator(task_id='start')

    trigger_job = SparkKubernetesOperator(
        task_id="trigger_job",
        namespace='kube-public',
        kubernetes_conn_id="kubernetes_default",
        application_file="/kubernetes/spark-pi.yaml",
        do_xcom_push=True,
        retries=3
    )

    # Thêm task check status
    check_status = SparkKubernetesSensor(
        task_id='check_status',
        namespace='kube-public',
        application_name="{{ task_instance.xcom_pull(task_ids='spark_task')['metadata']['name'] }}",
        kubernetes_conn_id="kubernetes_default",
        attach_log=True,
        poke_interval=30,
        timeout=600,
        retries=3,
    )

    # end dummy task
    end = DummyOperator(task_id='end')

    start >> trigger_job >> check_status >> end