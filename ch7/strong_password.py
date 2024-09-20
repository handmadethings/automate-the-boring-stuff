#! Python3

# strong_password.py - Detect wether a password is strong or not

import re

def strong_password_detector(password):
    '''Checks wether a password is strong, e.g.
    - Longer than 8 characters
    - Contains both upper and lower case letters
    - Contains at least one digit'''

    lowercase_regex = re.compile(r'([a-z]+)')
    uppercase_regex = re.compile(r'([A-Z]+)')
    digit_regex = re.compile(r'(\d+)')

    if len(password) > 8:
        if lowercase_regex.search(password):
            if uppercase_regex.search(password):
                if digit_regex.search(password):
                    print('Password accepted')
                    return True
                else:
                    print('Password must contain a digit')
                    return
            else:
                print('Password must contain at least one uppercase letter')
                return
        else:
            print('Password must contain at least one lowercase letter')
            return
    else:
        print('Password is too short')
        return

password_one = 'aZ09'
password_two = 'asdasdasd678'
password_three = 'SADFASDF567'
password_four = 'ASDFASDFsdfasdf'
password_five = '567898765435678'
password_six = 'ABCDabcd0'

strong_password_detector(password_one)
strong_password_detector(password_two)
strong_password_detector(password_three)
strong_password_detector(password_four)
strong_password_detector(password_five)
strong_password_detector(password_six)