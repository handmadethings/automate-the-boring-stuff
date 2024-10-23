import random, logging
logging.disable(logging.DEBUG)
logging.basicConfig(level=logging.DEBUG,
    format='%(asctime)s -  %(levelname)s -  %(message)s')
logging.debug('Start of program')
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    
logging.debug(f'Guess is {guess}')
toss = random.choice(('heads', 'tails'))
logging.debug(f'toss is {toss}')
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    logging.debug(f'toss is {toss}, guess is {guess}')
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')