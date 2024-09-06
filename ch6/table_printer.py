# table_printer.py
import copy

example_table_data = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def print_table(table_data):
    
    col_widths = [0] * len(table_data)

    copied_table_data = copy.deepcopy(table_data)

    for index, item in enumerate(copied_table_data):
        item.sort(key=lambda s: len(s), reverse=True)
        col_widths[index] = len(item[0])
    

    # for index, item in enumerate(table_data):
    #     print(f'item: {item}')
    #     print(f'Just: {col_widths[index]}')
    #     row_string = ' '.join(item)
    #     just = col_widths[index] + 40
    #     print(row_string.rjust(just))

    for i in range(len(table_data[0])):
        for j in range(len(table_data)):
            print(table_data[j][i].rjust(col_widths[j]), end=' ')
        print()


print_table(example_table_data)