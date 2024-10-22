#! python3
# large_file_deleter.py - Walks through a folder tree and searches for large files 

import os
from pathlib import Path

print('Find large files for deletion')
print('----------------------------------')
source_folder = input('What is the source folder?')
source_folder_path = Path(source_folder)

large_files = []

for foldername, subfolders, filenames in os.walk(source_folder_path):
    for filename in filenames:
        file_path = Path(foldername) / filename
        if os.path.getsize(file_path) > (100 * 10**6):
            large_files.append(file_path)

print('These files are quite large (>100Mb): ')
for i in large_files:
    print(i)