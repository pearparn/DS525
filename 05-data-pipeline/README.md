# Project 5: Creating and Scheduling Data Pipelines

## 1.Run Docker airflow

```
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.9.0/docker-compose.yaml'
```

## 2. Setting the right Airflow user

```
mkdir -p ./dags ./logs ./plugins ./config
echo -e "AIRFLOW_UID=$(id -u)" > .env
```

## 3.un Docker compose
```
docker compose up
```
## 4.Airflow
ไปที่ port 8080 เพื่อเข้าไปที่หน้า Airflow UI