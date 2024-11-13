#! python3
# blank_row_inserter.py - takes a (spreadsheet) filename and numbers N and M
# from the command line. Starting at row N, the program should insert M blank
# rows into the spreadsheet

import openpyxl, sys

if (args_count := len(sys.argv)) > 4:
    print(f"One argument expected, got {args_count - 1}")
    raise SystemExit(2)
elif args_count < 4:
    print("You need to provide three arguments;")
    print("the filename and two row numbers (int).")
    raise SystemExit(2)

