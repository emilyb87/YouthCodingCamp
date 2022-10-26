# craps.py
import random

DICE = '\U00002680\U00002681\U00002682\U00002683\U00002684\U00002685'

RULES = '''The Rules:

Played on a long green velvet table 'Craps' is the clasic casino dice game.
The game can go on indefinitely, with the tension and side bets mounting with each throw.

The rules are simple:

    The roller throws the dice.

    If she rolls a sum of 7 or 11 she wins.

    If she throws a sum of 2, 3 or 12 ("craps") she loses.

    Any other roll becomes her 'Point' and she continues to roll until either,
    i) she rolls her Point again and wins, or
    ii) she rolls a 7 and loses.
'''

print('++++++++++++++++++++++++++++++++++++++++++++++++++')
print(' \U0001F3B2 P L A Y   T H E   G A M E   O F   C R A P S \U0001F3B2')
print('--------------------------------------------------')
print()
print( RULES )
dummy = input('Press Enter to roll the dice...')
print()
die1 = random.randint(1,6)
die2 = random.randint(1,6)
total = die1 + die2
print('You rolled', die1, 'and', die2, 'for a sum of', total)
print()

# Check for win
if total == 7 or total == 11:
    print( 'Since you rolled', total, 'you win!' )
elif total == 2 or total == 3 or total == 12:
    print( 'Since you rolled', total, 'you lose!' )
else:
    print('Your Point is now', total )
    print('If you can roll', total,'again you will win,')
    print('but if you roll 7 first you will lose!')
    point = total
    over = False
    while not over:
        print()
        dummy = input('Press Enter to roll the dice...')
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        total = die1 + die2
        print()
        print('You rolled', die1, 'and', die2, 'for a sum of', total)
        if total == 7:
            print('Oh no you rolled 7, you lose!' )
            over = True
        elif total == point:
            print( 'You rolled your Point (', point, ') again so you win!' )
            over = True
        else:
            print('so you need to keep rolling!')
