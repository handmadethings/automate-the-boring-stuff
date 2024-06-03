def collatz(number):
    # integer_number = int(number)
    if number % 2 == 0:
        current_number = number // 2
        print(current_number)
        return current_number
    elif number % 2 == 1:
        current_number = 3 * number + 1
        print(current_number)
        return current_number
    
try:
    num = int(input("Please enter a positive integer: "))
    if num <= 0:
        negativeValueError = ValueError('Should be a positive number')
        raise negativeValueError
    while num != 1:
        num = collatz(num)
except ValueError:
    print("The number should be a positive integer")