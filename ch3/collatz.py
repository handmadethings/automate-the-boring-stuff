def collatz(number):
    integer_number = int(number)
    if integer_number % 2 == 0:
        current_number = number // 2
        print(current_number)
        return current_number
    elif integer_number % 2 == 1:
        current_number = 3 * integer_number + 1
        print(current_number)
        return current_number
    
try:
    num = input("Give me a number: ")
    while num != 1:
        num = collatz(num)
except ValueError:
    print("Please enter an integer")