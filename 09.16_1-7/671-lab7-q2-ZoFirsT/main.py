m = int(input())
n = int(input())

matrix = []
for _ in range(m):
    row = [int(input()) for _ in range(n)]
    matrix.append(row)

zero_count = [sum(1 for row in matrix if row[col] == 0) for col in range(n)]

print(matrix)
print(*zero_count, end=' ')
