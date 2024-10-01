# นำเข้าโมดูล math เพื่อใช้ฟังก์ชันคณิตศาสตร์ขั้นสูง เช่น การคำนวณรากที่สอง
import math

# สร้างลิสต์ว่างเพื่อเก็บตัวเลขที่ผู้ใช้ป้อน
numbers = []

# เริ่มลูปรับข้อมูลจากผู้ใช้
while True:
    # รับข้อมูลจากผู้ใช้
    user_input = input()
    
    # ตรวจสอบว่าผู้ใช้ต้องการจบการป้อนข้อมูลหรือไม่
    if user_input == 'q':
        break  # ออกจากลูปถ้าผู้ใช้ป้อน 'q'
    
    # แปลงข้อมูลที่รับมาเป็นตัวเลขทศนิยมและเพิ่มเข้าลิสต์
    numbers.append(float(user_input))

# ตรวจสอบว่ามีตัวเลขอย่างน้อย 2 ตัวในลิสต์หรือไม่
if len(numbers) < 2:
    print("At least two numbers are required.")
else:
    # คำนวณค่าเฉลี่ย (Mean)
    total = 0
    for num in numbers:
        total += num  # รวมค่าทั้งหมดในลิสต์
    average = total / len(numbers)  # หารด้วยจำนวนตัวเลขทั้งหมด

    # คำนวณค่าเบี่ยงเบนมาตรฐาน (Standard Deviation)
    sum_squared_diff = 0
    for num in numbers:
        # คำนวณผลต่างกำลังสองระหว่างแต่ละตัวเลขกับค่าเฉลี่ย
        sum_squared_diff += (num - average) ** 2
    
    # คำนวณความแปรปรวน (Variance) โดยใช้ n-1 สำหรับ sample standard deviation
    variance = sum_squared_diff / (len(numbers) - 1)
    
    # คำนวณค่าเบี่ยงเบนมาตรฐานโดยใช้รากที่สองของความแปรปรวน
    std_dev = math.sqrt(variance)

    # แสดงผลลัพธ์ โดยปัดเศษทศนิยมให้เหลือ 2 ตำแหน่ง
    print(f"{round(average, 2)} {round(std_dev, 2)}")