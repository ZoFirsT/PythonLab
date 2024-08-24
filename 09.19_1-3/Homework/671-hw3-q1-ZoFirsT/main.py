a = float(input())
b = float(input())
c = float(input())

if a <= 0 or b <= 0 or c <= 0:
    print("Invalid triangle")
elif a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Valid triangle")
        print("Equilateral")
    elif a == b or a == c or b == c:
        print("Valid triangle")
        print("Isosceles")
    else:
        print("Valid triangle")
        print("Scalene")
else:
    print("Invalid triangle")