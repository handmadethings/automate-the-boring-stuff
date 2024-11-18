#! python3
# remove_csv_header.py - Removes the header from all CSV files in the current
# working directory.

import csv, os

os.makedirs('headerRemoved', exist_ok=True)

# Loop through every file in the current working directory.
for csv_filename in os.listdir('.'):
    if not csv_filename.endswith('.csv'):
        continue    # skip non-csv files

    print(f'Removing header from {csv_filename}...')

    # TODO: Read the CSV file in (skipping first row).

    # TODO: Write out the CSV file.
