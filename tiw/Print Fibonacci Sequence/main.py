# ฟังก์ชัน fibonacci(n) สร้างลำดับฟีโบนักชีจำนวน n ตัว
def fibonacci(n):
    fib = [0, 1]  # เริ่มต้นด้วยสองตัวแรกของลำดับฟีโบนักชี
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])  # สร้างตัวถัดไปโดยบวกสองตัวก่อนหน้า
    return fib  # ส่งคืนลำดับฟีโบนักชีทั้งหมด

# ฟังก์ชัน print_fibonacci(x) พิมพ์ลำดับฟีโบนักชีจำนวน x ตัว
def print_fibonacci(x):
    if x < 2:
        print()  # ถ้า x น้อยกว่า 2 ให้พิมพ์บรรทัดว่าง
        return
    
    fib_sequence = fibonacci(x)  # สร้างลำดับฟีโบนักชี
    for i in range(0, x, 5):
        print(" ".join(map(str, fib_sequence[i:i+5])))  # พิมพ์ลำดับทีละ 5 ตัว

# รับค่า x จากผู้ใช้
x = int(input())
# เรียกใช้ฟังก์ชัน print_fibonacci เพื่อพิมพ์ลำดับฟีโบนักชี
print_fibonacci(x)
