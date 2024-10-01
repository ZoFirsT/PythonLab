k = int(input())

A = []

while True:
    user_input = input()
    if user_input == 'q':
        break
    A.append(float(user_input))

sum_first_k = sum(A[:k])
sum_last_k = sum(A[-k:])

print(sum_first_k + sum_last_k)
