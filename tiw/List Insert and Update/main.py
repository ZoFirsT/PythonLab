# สร้างลิสต์ว่างชื่อ A เพื่อเก็บตัวเลข
A = []

# วนลูป 5 ครั้งเพื่อรับข้อมูลจากผู้ใช้
for i in range(5):
    # รับข้อมูลจากผู้ใช้และแปลงเป็นจำนวนทศนิยม
    user_input = float(input())
    # เพิ่มข้อมูลที่รับมาเข้าไปในลิสต์ A
    A.append(user_input)

# รับค่า x จากผู้ใช้และแปลงเป็นจำนวนทศนิยม
x = float(input())

# วนลูปผ่านทุกสมาชิกในลิสต์ A
for i in range(len(A)):
    # เปรียบเทียบค่าในลิสต์ A กับค่า x
    if A[i] > x:
        # ถ้าค่าในลิสต์มากกว่า x ให้แทนที่ด้วย 'g' (greater)
        A[i] = 'g'
    elif A[i] < x:
        # ถ้าค่าในลิสต์น้อยกว่า x ให้แทนที่ด้วย 's' (smaller)
        A[i] = 's'
    else:
        # ถ้าค่าในลิสต์เท่ากับ x ให้แทนที่ด้วย 'e' (equal)
        A[i] = 'e'

# แสดงผลลัพธ์ของลิสต์ A หลังจากการเปรียบเทียบและแทนที่ค่า
print(A)