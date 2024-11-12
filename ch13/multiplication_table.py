#! python3
# multiplication_table.py - takes a number N from the command line and
# creates an N×N multiplication table in an Excel spreadsheet

import openpyxl, sys

if (args_count := len(sys.argv)) > 2:
    print(f"One argument expected, got {args_count - 1}")
    raise SystemExit(2)
elif args_count < 2:
    print("You need to provide one (int) argument; the size of the table")
    raise SystemExit(2)

try:
    table_size = int(sys.argv[1]) + 1
    print(f'Table size: {table_size}')
except ValueError:
    print('Please provide an integer argument')
    raise SystemExit(2)

for i in range(1, table_size):
    for j in range(1, table_size):
        product = i * j
        print(f'{i} x {j} is {product}')

# TODO: Create and populate workbook
wb = openpyxl.Workbook()
sheet = wb.active

sheet.title = 'Multiplication table'


# TODO: Save the Excel file
# wb.save('multiplicationtable.xlsx')