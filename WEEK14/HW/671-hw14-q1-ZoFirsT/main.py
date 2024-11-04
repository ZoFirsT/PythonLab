def remove_symbols(text):
    result = ""
    
    for char in text:
        if char.isalnum():
            result += char
            
    return "empty" if result == "" else result

input_text = input()

print(remove_symbols(input_text))
