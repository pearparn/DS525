# Project 6: Analytics Engineering

## 1.Run Docker compose

```
docker compose up
```
## 2.Port 3000
กรอก e-mail and pass

## 3. สร้าง Virtual Environment
```
python -m venv ENV
source ENV/bin/activate
```

## 4. ติดตั้ง dbt
```
pip install dbt-core dbt-postgres
dbt init
```
จากนั้นใส่ชื่อโปรเจค และเลือกว่าจะติดตั้ง database ตัวไหน
จากนั้นใส่ hostname "localhost" และใส่ username and pass
และกรอกข้อมูล

```
code /home/codespace/.dbt/profiles.yml
```
เพื่อ copy ไปสร้างไฟล์ profiles.yml ในโฟลเดอร์ ds525
## 5. dbt debug
```
cd ds525/
dbt debug
```
เพื่อดูว่าสามารถ connect ได้ไหม คือ All checks passed!

## 6. dbt run
```
dbt run
```
เพื่ออ่าน model ไป warehouse