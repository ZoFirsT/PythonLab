# รับค่าจำนวนเต็มจากผู้ใช้และเก็บไว้ในตัวแปร n
n = int(input())

# ตรวจสอบว่าค่าที่รับมาเป็นจำนวนบวกหรือไม่
while True:
    if n > 0:  # ถ้า n มากกว่า 0
        break  # ออกจากลูป
    else:  # ถ้า n ไม่มากกว่า 0
        n = int(input())  # รับค่าใหม่จากผู้ใช้

# วนลูปเพื่อสร้างสามเหลี่ยมตัวเลข
for i in range(1, n + 1):  # วนลูปจาก 1 ถึง n
    for j in range(1, i + 1):  # วนลูปจาก 1 ถึง i
        print(j, end=" ")  # พิมพ์ค่า j ตามด้วยช่องว่าง
    print()  # ขึ้นบรรทัดใหม่หลังจากพิมพ์แต่ละแถวเสร็จ