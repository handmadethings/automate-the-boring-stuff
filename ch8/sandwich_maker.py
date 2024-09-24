# ! Python3

# sandwich_maker.py - Make a sandwich using pyinputplus
import pyinputplus as pyip

menu = {'bread':{'wheat':2, 'white':1, 'sourdough':3},
          'protein':{'chicken':2, 'turkey':4, 'ham':3, 'tofu':2},
          'cheese':{'cheddar':1, 'swiss':2, 'mozzarella':3},
          'toppings':{'mayo':2, 'mustard':3,'lettuce':1, 'tomato':4}}


while True:
    price = 0
    bread = pyip.inputMenu(['wheat', 'white', 'sourdough'], prompt='What type of bread?')
    price += menu['bread'].get(bread)
    print(f'Price: {price}')

    protein = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], prompt='What type of protein?')
    price += menu['protein'].get(protein)
    print(f'Price: {price}')

    # cheese_yesnoo = pyip.inputYesNo('Do you want cheese?')

    if pyip.inputYesNo('Do you want cheese?') == 'yes':
        cheese = pyip.inputMenu(['cheddar', 'swiss', 'mozzarella'], prompt='What type of cheese?')
        menu['cheese'].get(cheese)
        price += menu['cheese'].get(cheese)
        print(f'Price: {price}')

    toppings = {}
    toppings['mayo'] = pyip.inputYesNo('Do you want mayo?')
    toppings['mustard'] = pyip.inputYesNo('Do you want mustard?')
    toppings['lettuce'] = pyip.inputYesNo('Do you want lettuce?')
    toppings['tomato'] = pyip.inputYesNo('Do you want tomato?')

    for key, value in toppings.items():
        if value == 'yes':
            price += menu['toppings'].get(key)

    how_many = pyip.inputInt('How many do you want?')

    total = how_many * price

    print(f'Your order:')
    print(f'Price: {price}')
    if how_many > 1:
        print(f'* {how_many} = {total}')
    break    