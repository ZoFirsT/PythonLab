def multiply_even_numbers(lst):
    even_numbers = [num for num in lst if num % 2 == 0]
    if not even_numbers:
        return -1
    result = 1
    for num in even_numbers:
        result *= num
    return result

n = int(input())
lst = [int(input()) for _ in range(n)]

result = multiply_even_numbers(lst)
print(result)
