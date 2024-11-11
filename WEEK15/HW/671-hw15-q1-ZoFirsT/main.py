# YOUR CODE HERE
import pandas as pd

def count_word(word):
    df = pd.read_csv('data.csv')

    count = 0

    for text in df['text']:
        count += text.count(word)

    return count

print(count_word(input()))