def remove_vowels():
    vowels = ['a', 'e', 'i', 'o', 'u']
    char_list = []
    
    while True:
        char = input()
        if char == '0':
            break
        char_list.append(char)
    
    for vowel in vowels:
        while vowel in char_list:
            char_list.remove(vowel)
    
    print(char_list)

remove_vowels()

