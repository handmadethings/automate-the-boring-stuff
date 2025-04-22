#! python3
# join_pdfs.py - Combines all the PDFs in a directory into into a single PDF.

import PyPDF2, os, sys
from pathlib import Path

pdf_files = []

print('Welcome to PDF Joiner 2')
path = input('At what path are the files located?')
new_filename = input('What would you like the new file to be called?')

if not new_filename.endswith('.pdf'):
    new_filename += '.pdf'

p = Path(path)

joined_file_path = p / new_filename

for filename in os.listdir(p):
     if filename.endswith('.pdf'):
         pdf_files.append(filename)

pdf_files.sort(key = str.lower)

pdf_writer = PyPDF2.PdfWriter()

# Loop through all the PDF files.
for filename in pdf_files:
    pdf_file_obj = open(p / filename, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file_obj)
    
    # Loop through all the pages (except the first) and add them.
    for page_num in range(len(pdf_reader.pages)):
        page_obj = pdf_reader.pages[page_num]
        print(f'Added {filename}')
        pdf_writer.add_page(page_obj)

# Save the resulting PDF to a file.
pdf_output = open(joined_file_path, 'wb')
pdf_writer.write(pdf_output)
print(f'Saving joined file as {new_filename}')
pdf_output.close()