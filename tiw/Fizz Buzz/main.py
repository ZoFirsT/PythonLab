# รับค่า n จากผู้ใช้และแปลงเป็นจำนวนเต็ม
n = int(input())

# วนลูปตั้งแต่ 1 ถึง n
for i in range(1, n + 1):
    # ตรวจสอบว่าตัวเลขหารด้วย 3 และ 5 ลงตัวหรือไม่
    if i % 3 == 0 and i % 5 == 0:
        print("Fizz Buzz", end=" ")  # ถ้าใช่ พิมพ์ "Fizz Buzz"
    # ตรวจสอบว่าตัวเลขหารด้วย 3 ลงตัวหรือไม่
    elif i % 3 == 0:
        print("Fizz", end=" ")  # ถ้าใช่ พิมพ์ "Fizz"
    # ตรวจสอบว่าตัวเลขหารด้วย 5 ลงตัวหรือไม่
    elif i % 5 == 0:
        print("Buzz", end=" ")  # ถ้าใช่ พิมพ์ "Buzz"
    # ถ้าไม่ตรงกับเงื่อนไขใดเลย
    else:
        print(i, end=" ")  # พิมพ์ตัวเลขนั้นๆ

# พิมพ์บรรทัดใหม่หลังจากจบลูป
print()
