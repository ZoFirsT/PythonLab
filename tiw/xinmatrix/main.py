# รับค่า m และ n จากผู้ใช้ ซึ่งเป็นขนาดของเมทริกซ์
m = int(input())  # จำนวนแถว
n = int(input())  # จำนวนคอลัมน์

# สร้างเมทริกซ์ว่างเปล่า
mat = []
# วนลูปเพื่อรับค่าสำหรับแต่ละแถวของเมทริกซ์
for i in range(m):
    row = []
    # วนลูปเพื่อรับค่าสำหรับแต่ละคอลัมน์ในแถวปัจจุบัน
    for j in range(n):
        num = int(input())  # รับค่าตัวเลขจากผู้ใช้
        row.append(num)  # เพิ่มตัวเลขลงในแถว
    mat.append(row)  # เพิ่มแถวที่สมบูรณ์ลงในเมทริกซ์

# รับค่า x จากผู้ใช้ เพื่อใช้ในการเปรียบเทียบ
x = int(input())

# สร้างเมทริกซ์ผลลัพธ์ว่างเปล่า
result = []

# วนลูปเพื่อสร้างเมทริกซ์ผลลัพธ์
for i in range(m):
    row = []
    for j in range(n):
        # เปรียบเทียบค่า x กับแต่ละองค์ประกอบในเมทริกซ์ mat
        if x > mat[i][j]:
            row.append('>')  # ถ้า x มากกว่า ใส่ '>'
        elif x < mat[i][j]:
            row.append('<')  # ถ้า x น้อยกว่า ใส่ '<'
        else:
            row.append('=')  # ถ้า x เท่ากับ ใส่ '='
    result.append(row)  # เพิ่มแถวผลลัพธ์ลงในเมทริกซ์ผลลัพธ์

# แสดงผลลัพธ์
print(result)