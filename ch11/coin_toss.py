import random, logging


logging.debug('Start of program')
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    
logging.debug(f'Guess is {guess}')
toss = random.randint(0, 1) # 0 is tails, 1 is heads
logging.debug(f'toss is {toss}')
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guesss = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')