# guessing_game 1.0
#
# The computer chooses a random number between 1 and 100 (inclusive).
#
# The user tries to guess the number and the computer tells them
# if they are high or low.
#
# Version 1.0
#
# Base version of the game. Just the functional core, no bells or whistles.

import random

secret_number = random.randint(1,100)

print( 'I have chosen a number from 1 to 100, try and guess it!' )
guess = int( input( 'Guess: ' ) )

while guess != secret_number :
    if guess > secret_number:
        print( 'Your guess is too high...' )
    elif guess < secret_number:
        print( 'Your guess is too low...' )
    guess = int( input( 'Guess: ' ) )

print( 'You got it! Well done.' )
