FROM apache/airflow:2.9.1-python3.10

# Establece la carpeta de trabajo donde vive Airflow
WORKDIR /opt/airflow

USER airflow

COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt
