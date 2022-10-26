# superhero.py
#
# Displays the user's super hero name
#
# Input: firstname lastname
# Output: super hero name

FIRST = [
    'CAPTAIN', 'TURBO', 'GALACTIC', 'THE', 'AQUA', 'FIRE',
    'IRON', 'SUPER', 'GREEN', 'PHANTOM', 'DARK', 'GHOST',
    'PROFESSOR', 'ATOMIC', 'ROCK', 'OMEGA', 'ROCKET',
    'SHADOW', 'AGENT', 'SILVER', 'WILD', 'WOLF', 'ULTRA',
    'WONDER', 'DOCTOR', 'STAR'
]

LAST = [
    'X', 'SHIELD', 'MACHINE', 'JUSTICE', 'BEAST', 'WING',
    'ARROW', 'SKULL', 'BLADE', 'BOLT', 'COBRA', 'BLAZE',
    'SOLDIER', 'STRIKE', 'FALCON', 'FANG', 'KING', 'SURFER',
    'BOT', 'GUARD', 'THING', 'CLAW', 'BRAIN', 'MASTER',
    'POWER', 'STORM'
]

print()
print('===========================================================')
print(' F I N D   O U T   Y O U R   S U P E R H E R O   N A M E !')
print('-----------------------------------------------------------')

# print( 'What is your super hero name? \U0001F9B8 \N{mage} \N{fairy} \U0001F9DC' )
print()
print( 'What is your full name? (first and last, no middle please)' )
name = input()

names = name.split()
hero_name = FIRST[ord(names[0][0].lower())-ord('a')] \
            + ' ' \
            + LAST[ord(names[1][0].lower())-ord('a')]
print()
print('Your super hero name is', hero_name, '\U0001F9B8')
print()
print('Go forth', hero_name, 'and be awesome!')