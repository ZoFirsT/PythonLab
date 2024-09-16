def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes(n):
    primes = [num for num in range(2, n + 1) if is_prime(num)]
    return primes

while True:
    try:
        n = int(input())
        if 1 < n < 1000:
            break
    except ValueError:
        pass

primes = find_primes(n)
print(*primes)
print(f"Total prime numbers: {len(primes)}")

