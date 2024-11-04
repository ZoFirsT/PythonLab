def count_vowels(text):
    vowels = {
        'a': 0,
        'e': 0,
        'i': 0,
        'o': 0,
        'u': 0
    }
    
    text = text.lower()
    
    for vowel in vowels:
        vowels[vowel] = text.count(vowel)
        
    for vowel, count in vowels.items():
        print(f"{vowel}: {count}")

text = input()

count_vowels(text)
