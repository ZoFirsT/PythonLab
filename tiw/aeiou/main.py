# สร้างรายการคำ
list_words = ['r', 'e', 'a', 'l', 'i', 'z', 'e']

# สร้างรายการสระ
vowels = ['a', 'e', 'i', 'o', 'u']

# สร้างรายการนับสระ โดยเริ่มต้นด้วยค่า 0 ทั้งหมด 5 ตัว (ตามจำนวนสระ)
countvowels = [0] * 5

# วนลูปผ่านแต่ละสระในรายการ vowels
for i in range(len(vowels)):
    # ตรวจสอบว่าสระปัจจุบันอยู่ในรายการคำหรือไม่
    if vowels[i] in list_words:
        # ถ้าพบสระในรายการคำ ให้เพิ่มค่าตัวนับที่ตำแหน่งเดียวกับสระนั้นขึ้น 1
        countvowels[i] += 1

# แสดงผลลัพธ์การนับสระ
print(countvowels)