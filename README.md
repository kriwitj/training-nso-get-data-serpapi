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