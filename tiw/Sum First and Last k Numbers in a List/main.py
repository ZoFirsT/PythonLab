# รับค่า k จากผู้ใช้และแปลงเป็นจำนวนเต็ม
k = int(input())

# สร้างลิสต์ว่างเพื่อเก็บตัวเลข
A = []

# วนลูปรับค่าจากผู้ใช้จนกว่าจะป้อน 'q'
while True:
    user_input = input()
    if user_input == 'q':  # ถ้าผู้ใช้ป้อน 'q' ให้ออกจากลูป
        break
    A.append(float(user_input))  # แปลงค่าเป็นทศนิยมและเพิ่มเข้าลิสต์

# คำนวณผลรวมของ k ตัวแรก
sum_first_k = sum(A[:k])

# คำนวณผลรวมของ k ตัวสุดท้าย
sum_last_k = sum(A[-k:])

# พิมพ์ผลรวมของ k ตัวแรกและ k ตัวสุดท้าย
print(sum_first_k + sum_last_k)
