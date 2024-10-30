char_list = []
while True:
    user_input = input()
    if user_input == '-1':
        break
    char_list.append(user_input)

counted = []

for char in sorted(char_list):
    if char not in counted:
        count = 0
        for check in char_list:
            if char == check:
                count += 1
        counted.append(char)
        print(f"{char}={count}", end=" ")