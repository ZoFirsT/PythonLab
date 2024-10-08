# รับค่า n จากผู้ใช้
# ใช้ลูป while เพื่อรับค่าจากผู้ใช้จนกว่าจะได้ค่าที่ถูกต้อง
while True:
    n = input("ใส่จำนวนเต็มคี่ที่มากกว่า 1: ")
    # ตรวจสอบว่าค่าที่รับเข้ามาเป็นตัวเลข, มากกว่า 1, และเป็นเลขคี่
    if n.isdigit() and int(n) > 1 and int(n) % 2 == 1:
        n = int(n)  # แปลงค่าเป็นตัวเลขจำนวนเต็ม
        break  # ออกจากลูปเมื่อได้ค่าที่ถูกต้อง
    print("กรุณาใส่จำนวนเต็มคี่ที่มากกว่า 1")  # แสดงข้อความเตือนถ้าค่าไม่ถูกต้อง

# วาดรูปแบบ
# ใช้ลูป for ซ้อนกันสองชั้นเพื่อวาดรูปแบบ
for i in range(n):  # ลูปภายนอกสำหรับแต่ละแถว
    for j in range(n):  # ลูปภายในสำหรับแต่ละคอลัมน์
        # ตรวจสอบเงื่อนไขเพื่อวาดดาวหรือขีด
        if i == 0 or i == n-1 or j == 0 or j == n-1 or i == j or i + j == n-1:
            print("*", end=" ")  # พิมพ์ดาวถ้าเป็นขอบหรือเส้นทแยงมุม
        else:
            print("-", end=" ")  # พิมพ์ขีดถ้าไม่ใช่ขอบหรือเส้นทแยงมุม
    print()  # ขึ้นบรรทัดใหม่หลังจากพิมพ์แต่ละแถวเสร็จ
