def find_duplicates(text):
    words = text.lower().split()
    
    word_counts = {}
    
    for word in words:
        clean_word = ''.join(c for c in word if c.isalnum())
        if clean_word:
            word_counts[clean_word] = word_counts.get(clean_word, 0) + 1
    
    duplicates = {word: count for word, count in word_counts.items() if count > 1}
    
    if duplicates:
        for word, count in sorted(duplicates.items()):
            print(f"{word}: {count}")
    else:
        print("no duplicated word")

text = input()

find_duplicates(text)
