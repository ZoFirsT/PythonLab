# นำเข้าไลบรารี numpy และตั้งชื่อย่อเป็น np
import numpy as np

# รับค่าจำนวนแถวและคอลัมน์จากผู้ใช้ โดยแยกด้วยช่องว่าง
rows, cols = map(int, input().split())
# rows = int(input())
# cols = int(input())

# อ่านเมทริกซ์จากไฟล์ matrix.txt โดยกำหนดชนิดข้อมูลเป็น int8 และตัดขนาดตามจำนวนแถวและคอลัมน์ที่รับมา
matrix = np.loadtxt('matrix.txt', dtype=np.int8)[:rows, :cols]

# แสดงเมทริกซ์ทั้งหมด
print(matrix)

# คำนวณและแสดงค่าเฉลี่ยของแต่ละคอลัมน์ โดยใช้ axis=0
# axis=0 (คำนวณค่าเฉลี่ยตามแนวตั้ง/columns)
col_means = np.mean(matrix, axis=0)
print(col_means)

# คำนวณและแสดงค่าเฉลี่ยของแต่ละแถว โดยใช้ axis=1
# axis=1 (คำนวณค่าเฉลี่ยตามแนวนอน/rows)
row_means = np.mean(matrix, axis=1)

print(row_means)



# x = [1, 2, 3, 4, 5]
# print(list(map(int, x)))