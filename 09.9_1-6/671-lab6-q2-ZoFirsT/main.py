def get_positive_integer():
    while True:
        try:
            n = int(input())
            if n > 0:
                return n
        except ValueError:
            pass
        except EOFError:
            return 0

def print_number_triangle(n):
    for i in range(1, n + 1):
        print(f"{i} " * i)

numbers = []
while True:
    n = get_positive_integer()
    if n == 0:
        break
    numbers.append(n)

for n in numbers:
    print_number_triangle(n)
    if n != numbers[-1]:
        print()
