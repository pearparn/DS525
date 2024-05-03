# Project 3: Building a Data Warehouse
## 1. สร้าง Virtual Environment
```
python -m venv ENV
```

## 2. Run requirements 
```
source ENV/bin/activate
pip install -r requirements.txt
pip freeze
```
เพื่อให้มั่นใจว่าใช้แพ็กเกจเวอร์ชั่นเดียวกัน

## 3. Run etl
```
python etl_bigquery.py 
```
เชื่อมต่อกับฐานข้อมูล Bigquery