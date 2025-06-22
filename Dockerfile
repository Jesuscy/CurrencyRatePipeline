FROM apache/airflow:2.9.1-python3.9

USER root
# Instala dependencias del sistema si necesitas
# RUN apt-get update && apt-get install -y libpq-dev gcc

USER airflow

# Copia requirements si necesitas
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
