# สร้างลิสต์เปล่าเพื่อเก็บคะแนนที่ถูกต้อง
listScore = []

# เริ่มลูปรับข้อมูลจากผู้ใช้
while True:
    # รับข้อมูลจากผู้ใช้
    score = input()
    
    # ตรวจสอบว่าผู้ใช้ต้องการจบการป้อนข้อมูลหรือไม่
    if score == "q":
        break  # ออกจากลูปถ้าผู้ใช้ป้อน 'q'
    
    # แปลงข้อมูลที่รับมาเป็นตัวเลขจำนวนเต็ม
    score = int(score)
    
    # ตรวจสอบว่าคะแนนอยู่ในช่วงที่ถูกต้องหรือไม่ (0-100)
    if 0 <= score <= 100:
        listScore.append(score)  # เพิ่มคะแนนที่ถูกต้องลงในลิสต์

# ตรวจสอบว่ามีคะแนนที่ถูกต้องในลิสต์หรือไม่
if listScore:
    # คำนวณค่าเฉลี่ยของคะแนน
    average = round(sum(listScore) / len(listScore), 2)
    
    # ตัดสินผลว่าผ่านเกณฑ์หรือไม่
    result = "Satisfactory" if average >= 50 else "Unsatisfactory"
    
    # แสดงผลลัพธ์
    print(f"{average} {result}")
else:
    # แสดงข้อความถ้าไม่มีคะแนนที่ถูกต้อง
    print("No valid scores entered.")