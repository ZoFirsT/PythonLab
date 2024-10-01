A = []

for i in range(5):
    user_input = float(input())
    A.append(user_input)

x = float(input())
for i in range(len(A)):
    if A[i] > x:
        A[i] = 'g'
    elif A[i] < x:
        A[i] = 's'
    else:
        A[i] = 'e'

print(A)
