# table_printer.py
import copy

example_table_data = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def print_table(table_data):
    
    col_widths = [0] * len(table_data)
    print(col_widths)

    copied_table_data = copy.deepcopy(table_data)

    for i in range(len(copied_table_data)):
        copied_table_data[i].sort(key=lambda s: len(s), reverse=True)
        print(copied_table_data[i])
        col_widths[i] = len(copied_table_data[i][0])

    print(col_widths)


print_table(example_table_data)