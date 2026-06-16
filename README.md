## การเตรียมสภาพแวดล้อม

### 1. ติดตั้ง Python

ดาวน์โหลด Python จาก [python.org](https://www.python.org/downloads/) แล้วติดตั้ง

> ติ๊ก **"Add Python to PATH"** ขณะติดตั้ง

ตรวจสอบว่าติดตั้งสำเร็จ:

```cmd
python --version
```

---

### 2. ติดตั้ง Library

เปิด Command Prompt แล้วรัน:

```cmd
pip install pandas requests openpyxl
```

> library อื่น (`os`, `json`, `time`) เป็น built-in ไม่ต้องติดตั้งเพิ่ม

---

### 3. สร้างไฟล์และรัน Script

#### เปิด Command Prompt แล้วไปยังโฟลเดอร์ที่ต้องการ

```cmd
cd "D:\training-nso-cafe-data"
```

#### สร้างไฟล์ Python

```cmd
type nul > serp-cafe-province.py
```

> เปิดไฟล์ด้วย Notepad หรือ VS Code แล้วนำโค้ดที่ได้จาก Prompt ด้านล่างไปวาง

#### รัน Script

```cmd
python serp-cafe-province.py
```

---

## Prompt สำหรับสร้าง Python Script ดึงข้อมูลคาเฟ่จาก Google Maps ผ่าน SerpAPI

```python
คุณเป็น Senior Python Developer ที่เชี่ยวชาญด้าน Web Scraping และ Google Maps Data Collection

สร้าง Python Script สำหรับดึงข้อมูลร้านคาเฟ่จาก Google Maps ผ่าน SerpAPI โดยใช้โครงสร้างเดียวกับตัวอย่างด้านล่างทุกประการ

ข้อกำหนด:

1. ใช้ Python

2. ใช้ libraries:

   * os
   * requests
   * json
   * time

3. กำหนด

API_KEY = "YOUR_API_KEY"

4. ใช้

base_url = "https://serpapi.com/search.json"

5. ค้นหาด้วย keyword

queries = ["cafe", "coffee"]

6. ดึงข้อมูลหลายหน้า

starts = [0,20,40,60,80,100]

7. จังหวัดที่ต้องการคือ

จังหวัด: {ชื่อจังหวัด}

8. หากระบุอำเภอเป็น "ทุกอำเภอ"

ให้สร้าง locations ครบทุกอำเภอของจังหวัดนั้น

ตัวอย่าง

locations = [
("อำเภอ1", lat, lon),
("อำเภอ2", lat, lon),
...
]

9. หากระบุรายชื่ออำเภอ

ให้สร้างเฉพาะอำเภอเหล่านั้น

10. ใช้พิกัดศูนย์กลางของแต่ละอำเภอ

11. สำหรับแต่ละอำเภอ

สร้างโฟลเดอร์

data/{ชื่ออำเภอ}

12. เรียก API ด้วย

params = {
    "engine": "google_maps",          # ใช้ Google Maps Engine
    "type": "search",                 # ค้นหาแบบ Search
    "q": q,                           # Keyword ที่ต้องการค้นหา (cafe, coffee)
    "ll": f"@{lat},{lon},11z",        # พิกัดศูนย์กลาง + ระดับ Zoom
    "nearby": "true",                 # ค้นหาเฉพาะสถานที่ใกล้พิกัด
    "google_domain": "google.co.th",  # ใช้ Google ประเทศไทย
    "hl": "th",                       # แสดงผลภาษาไทย
    "gl": "th",                       # ระบุประเทศเป็นประเทศไทย
    "start": start,                   # Offset สำหรับ Pagination
    "api_key": API_KEY                # SerpAPI API Key
}

13. บันทึกไฟล์เป็น

filename = f"{folder}/{q}*{start}*{district}.json"

14. ใช้

json.dump(
data,
f,
ensure_ascii=False,
indent=2
)

15. ใส่

time.sleep(1)

หลังเรียก API ทุกครั้ง

16. แสดง Progress

print("fetch:",district,q,start)

17. ส่งออกเฉพาะ Python Code

18. ห้ามอธิบาย

19. ห้ามตัดโค้ด

20. ต้องสามารถ Copy ไปรันได้ทันที

21. locations ต้องใส่ latitude และ longitude จริงของทุกอำเภอที่เลือก

22. ห้ามใส่ค่า Placeholder ใน locations

สร้างโค้ดตาม Template ด้านบน

จังหวัด: สระบุรี

อำเภอ:
- เมือง
- ...
```

### Data Dict

| Key | Description |
|------|-------------|
| `position` | ลำดับผลการค้นหาในรายการ |
| `title` | ชื่อสถานที่ / ชื่อร้าน |
| `place_id` | รหัส Place ID ของ Google Maps |
| `data_id` | รหัสข้อมูลภายในที่ใช้ระบุสถานที่ |
| `data_cid` | Customer ID (CID) ของสถานที่ใน Google Maps |
| `reviews_link` | URL สำหรับดึงข้อมูลรีวิวของสถานที่ |
| `photos_link` | URL สำหรับดึงรูปภาพของสถานที่ |
| `gps_coordinates` | พิกัดภูมิศาสตร์ของสถานที่ |
| `gps_coordinates.latitude` | ละติจูด |
| `gps_coordinates.longitude` | ลองจิจูด |
| `place_id_search` | URL สำหรับค้นหาสถานที่ด้วย Place ID |
| `provider_id` | รหัสผู้ให้บริการ/สถานที่จาก Google |
| `rating` | คะแนนรีวิวเฉลี่ย |
| `reviews` | จำนวนรีวิวทั้งหมด |
| `price` | ช่วงราคา |
| `extracted_price` | ระดับราคาในรูปแบบตัวเลข |
| `type` | ประเภทสถานที่หลัก |
| `types` | รายการประเภทสถานที่ทั้งหมด |
| `type_id` | รหัสประเภทสถานที่หลัก |
| `type_ids` | รายการรหัสประเภทสถานที่ |
| `address` | ที่อยู่ |
| `country` | ประเทศ |
| `open_state` | สถานะการเปิด-ปิดปัจจุบัน |
| `hours` | เวลาทำการแบบย่อ |
| `operating_hours` | เวลาทำการรายวัน |
| `phone` | เบอร์โทรศัพท์ |
| `website` | เว็บไซต์หรือเพจหลัก |
| `extensions` | ข้อมูลเสริมเกี่ยวกับร้าน |
| `service_options` | ตัวเลือกการให้บริการ |
| `user_review` | ตัวอย่างรีวิวจากผู้ใช้ |
| `thumbnail` | URL รูปภาพหน้าปกร้าน |
| `serpapi_thumbnail` | URL รูปภาพย่อผ่าน SerpAPI |

### Extensions

| Key | Description |
|------|-------------|
| `service_options` | รูปแบบการให้บริการ เช่น นั่งทาน สั่งกลับบ้าน |
| `highlights` | จุดเด่นของร้าน |
| `popular_for` | เหมาะสำหรับการใช้งานแบบใด |
| `offerings` | สิ่งที่ร้านมีให้บริการ |
| `dining_options` | ตัวเลือกอาหารหรือของหวาน |
| `amenities` | สิ่งอำนวยความสะดวก |
| `atmosphere` | บรรยากาศร้าน |
| `crowd` | กลุ่มลูกค้าที่นิยมมาใช้บริการ |
| `payments` | วิธีการชำระเงิน |
| `children` | ความเหมาะสมสำหรับเด็ก |
| `parking` | ข้อมูลที่จอดรถ |

### Service Options

| Key | Description |
|------|-------------|
| `นั่งรับประทานที่ร้าน` | สามารถนั่งรับประทานภายในร้านได้ |
| `สั่งกลับบ้าน` | สามารถสั่งกลับบ้านได้ |

### Operating Hours

| Key | Description |
|------|-------------|
| `วันจันทร์` | เวลาเปิด-ปิดวันจันทร์ |
| `วันอังคาร` | เวลาเปิด-ปิดวันอังคาร |
| `วันพุธ` | เวลาเปิด-ปิดวันพุธ |
| `วันพฤหัสบดี` | เวลาเปิด-ปิดวันพฤหัสบดี |
| `วันศุกร์` | เวลาเปิด-ปิดวันศุกร์ |
| `วันเสาร์` | เวลาเปิด-ปิดวันเสาร์ |
| `วันอาทิตย์` | เวลาเปิด-ปิดวันอาทิตย์ |
