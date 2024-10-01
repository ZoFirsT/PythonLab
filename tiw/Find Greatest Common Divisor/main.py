a = int(input())
b = int(input())

if a > b:
    a, b = b, a

while b != 0:
    a, b = b, a % b

print(a)
