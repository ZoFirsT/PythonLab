m, n = int(input()), int(input())

matrix = []
for i in range(m):
    row = []
    for j in range(n):
        element = int(input())
        row.append(element)
    matrix.append(row)

zero_count = []
for col in range(n):
    count = 0
    for row in range(m):
        if matrix[row][col] == 0:
            count += 1
    zero_count.append(count)

print(matrix)
print(*zero_count, end=' ')
