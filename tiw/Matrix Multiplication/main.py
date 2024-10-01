# รับค่า n จากผู้ใช้
n = int(input())

# สร้างฟังก์ชันสำหรับรับข้อมูล matrix
def input_matrix(n):
    matrix = []
    for _ in range(n):
        row = [int(input()) for _ in range(n)]
        matrix.append(row)
    return matrix

# รับข้อมูล matrix A และ B
A = input_matrix(n)
B = input_matrix(n)

# สร้างฟังก์ชันสำหรับคูณ matrix
def multiply_matrices(A, B):
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]
    return result

# คำนวณผลคูณของ matrix A และ B
C = multiply_matrices(A, B)

# แสดงผลลัพธ์
print(A)
print(B)
print(C)
