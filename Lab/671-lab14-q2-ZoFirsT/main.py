text = input()
words = text.split(',')

try:
    age = int(words[2])
    print(f"{words[1]}, {words[0]} is a {words[3]} student and is {age} years old.")
except ValueError:
    print("invalid input")
