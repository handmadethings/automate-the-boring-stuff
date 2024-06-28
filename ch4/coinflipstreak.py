import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    heads_tails_list = []
    for i in range(100):
        heads_or_tails = random.randint(0, 1)
        if heads_tails_list == 1:
            heads_tails_list.append('H')
        else:
            heads_tails_list.append('T')

    # Code that checks if there is a streak of 6 heads or tails in a row.
print('Chance of streak: %s%%' % (numberOfStreaks / 100))