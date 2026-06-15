## Prompt สำหรับสร้าง Python Script ดึงข้อมูลคาเฟ่จาก Google Maps ผ่าน SerpAPI

คุณเป็น Senior Python Developer ที่เชี่ยวชาญด้าน Web Scraping และ Google Maps Data Collection

สร้าง Python Script สำหรับดึงข้อมูลร้านคาเฟ่จาก Google Maps ผ่าน SerpAPI โดยใช้โครงสร้างเดียวกับตัวอย่างด้านล่างทุกประการ

---

## ข้อกำหนด

### 1. ใช้ Python

### 2. ใช้ Libraries

```python
import os
import requests
import json
import time
```

### 3. กำหนด API Key

```python
API_KEY = "YOUR_API_KEY"
```

### 4. Base URL

```python
base_url = "https://serpapi.com/search.json"
```

### 5. Keyword สำหรับค้นหา

```python
queries = ["cafe", "coffee"]
```

### 6. ดึงข้อมูลหลายหน้า

```python
starts = [0,20,40,60,80,100]
```

### 7. จังหวัดที่ต้องการ

```text
จังหวัด: <PROVINCE_NAME>
```

### 8. กรณีเลือก "ทุกอำเภอ"

ให้สร้าง `locations` ครบทุกอำเภอของจังหวัด

ตัวอย่าง

```python
locations = [
    ("อำเภอ1", lat, lon),
    ("อำเภอ2", lat, lon),
    ("อำเภอ3", lat, lon)
]
```

### 9. กรณีระบุรายชื่ออำเภอ

ให้สร้างเฉพาะอำเภอที่ระบุ

### 10. ใช้พิกัดศูนย์กลางของแต่ละอำเภอ

* ต้องเป็น Latitude และ Longitude จริง
* ห้ามใช้ Placeholder
* ห้ามใช้ค่าประมาณ

### 11. สร้างโฟลเดอร์สำหรับแต่ละอำเภอ

รูปแบบ

```text
data/{ชื่ออำเภอ}
```

ตัวอย่าง

```text
data/เมืองเชียงใหม่
data/สารภี
data/หางดง
```

### 12. เรียก SerpAPI

```python
params = {
    "engine":"google_maps",
    "type":"search",
    "q":q,
    "ll":f"@{lat},{lon},11z",
    "nearby":"true",
    "google_domain":"google.co.th",
    "hl":"th",
    "gl":"th",
    "start":start,
    "api_key":API_KEY
}
```

### 13. บันทึกไฟล์

```python
filename = f"{folder}/{q}_{start}_{district}.json"
```

### 14. ใช้ json.dump

```python
json.dump(
    data,
    f,
    ensure_ascii=False,
    indent=2
)
```

### 15. หน่วงเวลา

หลังเรียก API ทุกครั้ง

```python
time.sleep(1)
```

### 16. แสดง Progress

```python
print("fetch:",district,q,start)
```

### 17. รูปแบบผลลัพธ์

* ส่งออกเฉพาะ Python Code
* ห้ามอธิบาย
* ห้ามใส่ Markdown รอบโค้ด
* ห้ามตัดโค้ด
* ต้องสามารถ Copy ไปรันได้ทันที

### 18. ข้อกำหนด Locations

* ต้องใส่ Latitude จริง
* ต้องใส่ Longitude จริง
* ต้องใส่ครบทุกอำเภอที่เลือก
* ห้ามใช้ Placeholder
* ห้ามใช้ Dummy Data

---

## งานที่ต้องทำ

สร้างโค้ดตาม Template ด้านบน โดยใช้ข้อมูลต่อไปนี้

```text
จังหวัด: <PROVINCE_NAME>

อำเภอ:
- <เมือง>
- <อำเภออื่น ๆ>
```