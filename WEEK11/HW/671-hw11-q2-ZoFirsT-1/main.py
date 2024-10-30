def list_manipulation(list, command, location, value):
    if command == "remove":
        if location == "end":
            list.pop()
        elif location == "beginning":
            list.pop(0)
    elif command == "add":
        if location == "end":
            list.append(value)
        elif location == "beginning":
            list.insert(0, value)
    return list

A = []
for i in range(3):
    num = input()
    A.append(num)

command = input()
location = input()
value = input()

result = list_manipulation(A, command, location, value)

print(result)