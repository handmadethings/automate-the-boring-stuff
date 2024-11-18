#! python3
# join_pdfs.py - Combines all the PDFs in a directory into into a single PDF.

import PyPDF2, os, sys
from pathlib import Path

pdf_files = []

if (args_count := len(sys.argv)) > 3:
    print(f"Two arguments expected, got {args_count - 1}")
    raise SystemExit(2)
elif args_count < 3:
    print("You need to provide two arguments; the path and joined filename")
    raise SystemExit(2)

p = Path(sys.argv[1])
joined_file_path = p / sys.argv[2]

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
        pdf_writer.add_page(page_obj)

# Save the resulting PDF to a file.
pdf_output = open(joined_file_path, 'wb')
pdf_writer.write(pdf_output)
pdf_output.close()