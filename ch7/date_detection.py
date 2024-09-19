#! Python3

# date_detection.py - Detect dates in the DD/MM/YYYY format

import re, calendar

date_regex = re.compile(r'([0-3]\d)/([01]\d)/([1-2]\d{3})')

test_string_one = '31/06/299'
test_string_two = '31/02/1984'

def date_detection(date_string):
    date_regex = re.compile(r'([0-3]\d)/([01]\d)/([1-2]\d{3})')
    groups = date_regex.findall(date_string)

    if groups==[]:
        print('Invalid date format')
        return 'Invalid date format'

    for day,month,year in groups:
        day=int(day)
        month=int(month)
        year=int(year)

    if (month==4 or month==6 or month==9 or month==11):
        if day==31:
            print('Invalid no of days for month')
            return 'Invalid date format'

    elif month == 2:
        if calendar.isleap(year):
            if not day in range(1,30):
                print('Invalid no of days for leap year')
                return 'Invalid date format'
        else:
            if not day in range(1,29):
                print('Invalid no of days')
                return 'Invalid date format'
    else:
        print('Valid date')
        return 'Valid date'

date_detection(test_string_one)
date_detection(test_string_two)