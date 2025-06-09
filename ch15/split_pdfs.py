#! python3
# split_pdfs.py - Spit a PDF into separate pages.

import PyPDF2, os, sys
from pathlib import Path

print('Welcome to PDF Joiner 2')
path = input('At what path are the files located?')
file_name = input('What is the filename?')

if not file_name.endswith('.pdf'):
    file_name += '.pdf'

p = Path(path)

file_path = p / file_name

pdf_file_obj = open(file_path, 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file_obj)


for page_num in range(len(pdf_reader.pages)):
    print(f'page_num: {page_num}')
    page_obj = pdf_reader.pages[page_num]
    pdf_writer = PyPDF2.PdfWriter()
    pdf_writer.add_page(page_obj)
    new_file_name = f'{page_num}. {file_name}'
    joined_file_path = p / new_file_name
    pdf_output = open(joined_file_path, 'wb')
    pdf_writer.write(pdf_output)
    print(f'Saving joined file as {new_file_name}')
    pdf_output.close()

print('Finished')