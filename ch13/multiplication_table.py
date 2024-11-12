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
except ValueError:
    print('Please provide an integer argument')
    raise SystemExit(2)

wb = openpyxl.Workbook()
sheet = wb['Sheet']

for i in range(1, table_size):
    index_column = f'A{i+1}'
    sheet[index_column] = i
    index_column = openpyxl.utils.get_column_letter(i+1)
    index_row = f'{index_column}1'
    sheet[index_row] = i
    for j in range(1, table_size):
        column = openpyxl.utils.get_column_letter(i+1)
        row = j + 1
        product = i * j
        index = f'{column}{row}'
        sheet[index] = product

wb.save('multiplicationtable.xlsx')