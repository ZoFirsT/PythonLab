x = int(input())
y = int(input())

if y <= 0:
    print("Unable to create a table")
else:
    i = 1
    while i <= y:
        result = x * i
        print(f"{x}*{i}={result}")
        i += 1