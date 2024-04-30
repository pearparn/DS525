# Project 3: Building a Data Warehouse
Redshift
## 1. Run docker compose
```
docker compose up
```
เพื่อเชื่อมต่อ cassandra

## 2. Run requirements 
```
python -m venv ENV
source ENV/bin/activate
pip install -r requirements.txt
pip freeze
```
เพื่อให้มั่นใจว่าใช้แพ็กเกจเวอร์ชั่นเดียวกัน

## 3. Run etl
```
python etl.py 
```
เชื่อมต่อกับฐานข้อมูล Cassandra, สร้าง และใส่ข้อมูลลงในตาราง