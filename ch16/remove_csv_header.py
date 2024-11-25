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

    # Read the CSV file in (skipping first row).
    csv_rows = []
    csv_file_object = open(csv_filename)
    reader_object = csv.reader(csv_file_object)
    for row in reader_object:
        if reader_object.line_num == 1:
            continue    # Skip the first row
        csv_rows.append(row)
    csv_file_object.close

    # Write out the CSV file.´
    csv_file_object = open(os.path.join('headerRemoved', csv_filename), 'w',
                           newline='')
    csv_writer = csv.writer(csv_file_object)
    for row in csv_rows:
        csv_writer.writerow(row)
    csv_file_object.close()
