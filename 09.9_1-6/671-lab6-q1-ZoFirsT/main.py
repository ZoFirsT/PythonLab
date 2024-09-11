def print_matrix(n, x, y):
    for i in range(n):
        for j in range(n):
            print(f"({i},{j})", end=" ")
            if i == x and j == y:
                break
        print()
        if i == x:
            break

n = int(input())
x = int(input())
y = int(input())

print_matrix(n, x, y)
