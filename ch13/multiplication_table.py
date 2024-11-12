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

# TODO: Create and populate workbook
# wb = openpyxl.Workbook()
# sheet = wb['Sheet']

for i in range(1, table_size):
    print(f'Set the value of row 1 column {i} to {i}')
    index_column = f'A{i}'
    sheet[index_column] = i
    print(f'Set the value of column 1 row {i} to {i}')
    column = openpyxl.utils.get_column_letter(i)
    index_row = f'1{column}'
    sheet[index_row] = i
    for j in range(1, table_size):
        product = i * j
        print(f'Row {i} column {j} should have the value {product}')
        # print(f'{i} x {j} is {product}')

# TODO: Save the Excel file
# wb.save('multiplicationtable.xlsx')