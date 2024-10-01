# สามารถเปลี่ยนเป็นรับค่าจาก input ได้
list_words = ['r', 'e', 'a', 'l', 'i', 'z', 'e']
vowels = ['a', 'e', 'i', 'o', 'u']
countvowels = [0]*5

for i in range(len(vowels)):
    if vowels[i] in list_words:
        countvowels[i] += 1

print(countvowels)
