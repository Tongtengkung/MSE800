import pandas as pd


with open('sample_text.txt', 'r') as file:
    text_content = file.read()
    count_double_underscores = text_content.count('__')
print(f"Number of '__' in the text file: {count_double_underscores}")