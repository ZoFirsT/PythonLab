dele = ['a', 'e', 'i', 'o', 'u']

user_list = []

while True:
    item = input()
    if item == '0':
        break
    user_list.append(item)

    for d in dele:
        while d in user_list:
            user_list.remove(d)
    

print(user_list)