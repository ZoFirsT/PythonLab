x = int(input())
y = int(input())
d = int(input())

count = 0

for num in range(x, y+1):
    if num % d == 0:
        print(num, end=' ')
        count += 1


print(f'count={count}')