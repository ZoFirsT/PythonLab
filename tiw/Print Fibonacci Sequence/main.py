def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

def print_fibonacci(x):
    if x < 2:
        print()
        return
    
    fib_sequence = fibonacci(x)
    for i in range(0, x, 5):
        print(" ".join(map(str, fib_sequence[i:i+5])))

x = int(input())
print_fibonacci(x)
