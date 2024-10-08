# คำอธิบายโค้ดแบบละเอียด:

# สร้างลิสต์ว่างเพื่อเก็บตัวเลข
numbers = []

# วนลูป 10 ครั้งเพื่อรับข้อมูลจากผู้ใช้
for i in range(10):
    # รับข้อมูลจากผู้ใช้และแปลงเป็นจำนวนเต็ม
    user_input = int(input())
    # เพิ่มตัวเลขที่รับมาเข้าไปในลิสต์ numbers
    numbers.append(user_input)

# วนลูปผ่านทุกตัวเลขในลิสต์ numbers
for number in numbers:
    # ตรวจสอบว่าตัวเลขปัจจุบันเป็น 0 หรือไม่
    if number == 0:
        # ถ้าเป็น 0 ให้ลบออกจากตำแหน่งปัจจุบัน
        numbers.remove(number)
        # แล้วเพิ่ม 0 กลับเข้าไปที่ท้ายลิสต์
        numbers.append(number)

# แสดงผลลัพธ์ของลิสต์ numbers หลังจากย้าย 0 ไปท้ายลิสต์แล้ว
print(numbers)

# หมายเหตุ: วิธีนี้อาจไม่มีประสิทธิภาพสำหรับลิสต์ขนาดใหญ่
# เนื่องจากการลบและเพิ่มสมาชิกในลิสต์หลายครั้ง
# อาจทำให้เกิดการย้ายข้อมูลในหน่วยความจำบ่อยครั้ง