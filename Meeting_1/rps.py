# rps.py
import random

print()
print(':::::::::::::::::::::::::::::::::::::::::::::::::::')
print(' P L A Y   R O C K - P A P E R - S C I S S O R S !')
print(':::::::::::::::::::::::::::::::::::::::::::::::::::')
print()
print( 'Remember rock crushes scissors, scissors cuts paper, and paper wraps up rock!' )
print()
print( 'Rock -> R' )
print( 'Paper -> P' )
print( 'Scissors -> S')
print()
player = input( 'Your move? (R|P|S) ' )

computer = random.randint(1,3)
if computer == 1:
    computer = 'R'
elif computer == 2:
    computer = 'P'
else:
    computer = 'S'

print()
print( 'The computer played', computer )
print()

if player == 'R':
    if computer == 'P':
        print( 'Paper wraps Rock so the computer wins!' )
    elif computer == 'S':
        print( 'Rock crushes Scissors so you win!' )
    else:
        print( "You both played Rock so it's a tie!" )
elif player == 'P':
    if computer == 'R':
        print( 'Paper wraps Rock so you win!' )
    elif computer == 'S':
        print( 'Scissors cuts paper so the computer wins!' )
    else:
        print( "You both played Paper so it's a tie." )
elif player == 'S':
    if computer == 'R':
        print( 'Rock crushses scissors so the computer wins!' )
    elif computer == 'P':
        print( 'Paper wraps rock so you win!' )
    else:
        print( 'You both played Scissors so it is a tie!' )
else:
    print('I don\'t recognize your move. Choose R or P or S next time.')
