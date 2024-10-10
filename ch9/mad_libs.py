#! python3
# mad_libs.py - Mad Libs program that reads in text files and lets the user
# add their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB
# appears in the text file.

import re
from pathlib import Path

# Get the path to the file to read
directory = input('Where is the file located? ')
file_name = input('What is the file name? ')
file_name += '.txt'

p = Path(directory) / file_name

regex = re.compile(r'(ADJECTIVE)|(NOUN)|(VERB)|(ADVERB)')

# Open the file in write mode
with open(Path(directory) / file_name, 'r') as read_file:
    text = read_file.read()

for i in regex.findall(text):
    for j in i:
        if j != '':
            reg = re.compile(f'{j}')
            input_text = input(f'Enter a {j}: ')
            text = reg.sub(input_text, text, 1)

print(text)

new_file_name = f'ans_{file_name}.txt'

with open(Path(directory) / new_file_name, 'w') as write_file:
    text = write_file.write(text)