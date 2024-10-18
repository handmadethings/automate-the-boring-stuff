#! python3
# selective_copy.py - Walks through a folder tree and searches for files with
# a certain file extension (e.g. .pdf or .jpg), adn copies these files
# to a new folder.

import os, shutil
from pathlib import Path

print('Copy Specific file types in a tree')
print('----------------------------------')
source_folder = input('What is the source folder?')
source_folder_path = Path(source_folder)
destination_folder = input('What is the destination folder?')
destination_folder_path = Path(destination_folder)
file_type = input('What file type (e.g. pdf, jpeg, docx)?')

for foldername, subfolders, filenames in os.walk(source_folder_path):
    for filename in filenames:
        if filename.endswith(file_type):
            file_path = Path(foldername) / filename
            print(f'Copying {filename}')
            shutil.copy(file_path, destination_folder_path)
print('Done!')