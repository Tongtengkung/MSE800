import pandas as pd


with open('sample_text.txt', 'r') as file:                                  # Open the text file in read mode       
    text_content = file.read()                                              # Read the content of the file into a string
    count_double_underscores = text_content.count('__')                     # Count the occurrences of '__' in the text content
print(f"Number of '__' in the text file: {count_double_underscores}")       # Print the count of '__' in the text file