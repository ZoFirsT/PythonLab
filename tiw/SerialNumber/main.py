x = int(input())
y = int(input())

result = []
for i in range(1, y + 1):
    term = int(str(x) * i)
    result.append(str(term))

print(','.join(result))
# print(result)


# n = int(input())
# for i in range(n):
#     print(i + 1)