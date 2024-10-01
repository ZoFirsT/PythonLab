# รับค่า n จากผู้ใช้
while True:
    n = input("ใส่จำนวนเต็มคี่ที่มากกว่า 1: ")
    if n.isdigit() and int(n) > 1 and int(n) % 2 == 1:
        n = int(n)
        break
    print("กรุณาใส่จำนวนเต็มคี่ที่มากกว่า 1")

# วาดรูปแบบ
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1 or i == j or i + j == n-1:
            print("*", end=" ")
        else:
            print("-", end=" ")
    print()
