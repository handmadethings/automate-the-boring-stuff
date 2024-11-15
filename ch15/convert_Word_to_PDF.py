# This script runs on Windows only, and you must have Word installed.
import win32com.client # install with "pip install pywin32==224"
import docx

word_filename = 'your_word_document.docx'
pdf_filename = 'your_pdf_filename.pdf'

doc = docx.Document()
# Code to create Word document goes here.
doc.save(wordFilename)

wd_format_PDF = 17 # Word's numeric code for PDFs.
word_obj = win32com.client.Dispatch('Word.Application')

doc_obj = word_obj.Documents.Open(wordFilename)
doc_obj.SaveAs(pdf_filename, FileFormat=wd_format_PDF)
doc_obj.Close()
word_obj.Quit()