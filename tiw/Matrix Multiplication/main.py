# รับค่า n จากผู้ใช้
# n คือขนาดของเมทริกซ์จัตุรัส (n x n)
n = int(input())

# สร้างฟังก์ชันสำหรับรับข้อมูล matrix
def input_matrix(n):
    # สร้างลิสต์ว่างเพื่อเก็บเมทริกซ์
    matrix = []
    # วนลูป n ครั้งเพื่อรับข้อมูลแต่ละแถวของเมทริกซ์
    for _ in range(n):
        # สร้างแถวโดยรับค่า n ตัวจากผู้ใช้และแปลงเป็นจำนวนเต็ม
        row = [int(input()) for _ in range(n)]
        # เพิ่มแถวลงในเมทริกซ์
        matrix.append(row)
    # ส่งคืนเมทริกซ์ที่สร้างเสร็จแล้ว
    return matrix

# รับข้อมูล matrix A และ B
# เรียกใช้ฟังก์ชัน input_matrix สองครั้งเพื่อรับข้อมูลเมทริกซ์ A และ B
A = input_matrix(n)
B = input_matrix(n)

# สร้างฟังก์ชันสำหรับคูณ matrix
def multiply_matrices(A, B):
    # สร้างเมทริกซ์ผลลัพธ์ขนาด n x n โดยเริ่มต้นด้วยค่า 0 ทั้งหมด
    result = [[0 for _ in range(n)] for _ in range(n)]
    # วนลูปเพื่อคำนวณค่าแต่ละตำแหน่งในเมทริกซ์ผลลัพธ์
    for i in range(n):
        for j in range(n):
            for k in range(n):
                # คำนวณผลคูณและบวกสะสมในแต่ละตำแหน่ง
                result[i][j] += A[i][k] * B[k][j]
    # ส่งคืนเมทริกซ์ผลลัพธ์
    return result

# คำนวณผลคูณของ matrix A และ B
# เรียกใช้ฟังก์ชัน multiply_matrices เพื่อคูณเมทริกซ์ A และ B
C = multiply_matrices(A, B)

# แสดงผลลัพธ์
# แสดงเมทริกซ์ A, B และผลลัพธ์ C ตามลำดับ
print(A)
print(B)
print(C)
