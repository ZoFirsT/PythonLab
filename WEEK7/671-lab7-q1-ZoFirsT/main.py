k = int(input())

A = []

while True:
    user_input = input()
    if user_input == 'q':
        break
    A.append(float(user_input))

if len(A) < k:
    print("Invalid")
else:
    sum_first_k = sum(A[:k])
    sum_last_k = sum(A[-k:])
    total_sum = sum_first_k + sum_last_k
    
    print(total_sum)
