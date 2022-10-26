# wordle.py

import random

WORDS = [
    'Aargh', 'Aback', 'Abaft', 'Aboon', 'About', 'Above', 'Abuse', 'Accel', 'Acute', 'Adieu',
    'Adios', 'Admit', 'Adopt', 'Adown', 'Adult', 'Afoot', 'Afore', 'Afoul', 'After', 'Again',
    'Agape', 'Agent', 'Agogo', 'Agone', 'Agree', 'Ahead', 'Ahull', 'Alack', 'Alcon', 'Alife',
    'Alike', 'Aline', 'Alive', 'Allow', 'Aloft', 'Aloha', 'Alone', 'Along', 'Aloof', 'Aloud',
    'Alter', 'Amiss', 'Among', 'Amply', 'Amuck', 'Anger', 'Angry', 'Apace', 'Apart', 'Apple',
    'Apply', 'Aptly', 'Arear', 'Argue', 'Arise', 'Aside', 'Askew', 'Aught', 'Avast', 'Avoid',
    'Award', 'Aware', 'Awful', 'Badly', 'Bakaw', 'Bally', 'Basic', 'Basis', 'Basta', 'Beach',
    'Begad', 'Begin', 'Below', 'Birth', 'Black', 'Blame', 'Bless', 'Blige', 'Blind', 'Block',
    'Blood', 'Board', 'Bothe', 'Brain', 'Brava', 'Brave', 'Bravo', 'Bread', 'Break', 'Brief',
    'Bring', 'Broad', 'Brown', 'Build', 'Burst', 'Buyer', 'Canny', 'Carry', 'Catch', 'Cause',
    'Chain', 'Chair', 'Cheap', 'Check', 'Chest', 'Chief', 'Child', 'China', 'Chook', 'Circa',
    'Civil', 'Claim', 'Class', 'Clean', 'Clear', 'Climb', 'Clock', 'Close', 'Coach', 'Coast',
    'Count', 'Court', 'Cover', 'Coyly', 'Crazy', 'Cream', 'Crime', 'Cross', 'Crowd', 'Crown',
    'Cycle', 'Daily', 'Damme', 'Dance', 'Death', 'Depth', 'Dildo', 'Dimly', 'Dirty', 'Ditto',
    'Doubt', 'Draft', 'Drama', 'Dream', 'Dress', 'Drily', 'Drink', 'Drive', 'Dryly', 'Dully',
    'Early', 'Earth', 'Empty', 'Enemy', 'Enjoy', 'Enter', 'Entry', 'Equal', 'Error', 'Event',
    'Exact', 'Exist', 'Extra', 'Faint', 'Faith', 'False', 'Fatly', 'Fault', 'Feyly', 'Field',
    'Fifth', 'Fight', 'Final', 'First', 'Fitly', 'Floor', 'Focus', 'Force', 'Forte', 'Forth',
    'Frame', 'Frank', 'Fresh', 'Frick', 'Front', 'Fruit', 'Fudge', 'Fully', 'Funny', 'Furth',
    'Gaily', 'Gayly', 'Giant', 'Glass', 'Godly', 'Golly', 'Grand', 'Grant', 'Grass', 'Gratz',
    'Great', 'Green', 'Gross', 'Group', 'Guess', 'Guide', 'Hallo', 'Haply', 'Happy', 'Harsh',
    'Hasta', 'Havoc', 'Heart', 'Heavy', 'Hella', 'Hello', 'Hence', 'Henry', 'Horse', 'Hotel',
    'Hotly', 'House', 'Howay', 'Howdy', 'Hullo', 'Human', 'Huzza', 'Icily', 'Ideal', 'Image',
    'Imply', 'Index', 'Infra', 'Inner', 'Input', 'Intl.', 'Issue', 'Japan', 'Jesus', 'Jildi',
    'Joint', 'Jolly', 'Jones', 'Judge', 'Kapow', 'Knife', 'Large', 'Laugh', 'Laura', 'Laxly',
    'Layer', 'Learn', 'Leave', 'Legal', 'Lento', 'Let’s', 'Level', 'Lewis', 'Light', 'Limit',
    'Local', 'Loose', 'Lordy', 'Lowly', 'Lucky', 'Lunch', 'Madly', 'Magic', 'Major', 'March',
    'Marry', 'Match', 'Maybe', 'Mercy', 'Metal', 'Minor', 'Minus', 'Model', 'Money', 'Month',
    'Moral', 'Motor', 'Mouth', 'Music', 'Naked', 'Nasty', 'Naval', 'Neath', 'Never', 'Newly',
    'Night', 'Nobly', 'Noise', 'North', 'Novel', 'Nurse', 'Occur', 'Oddly', 'Offer', 'Often',
    'One’s', 'Order', 'Other', 'Ought', 'Outer', 'Owner', 'Panel', 'Paper', 'Party', 'Peace',
    'Peter', 'Phase', 'Phone', 'Piano', 'Piece', 'Pilot', 'Pitch', 'Place', 'Plain', 'Plane',
    'Plant', 'Plate', 'Plonk', 'Plumb', 'Point', 'Pound', 'Power', 'Press', 'Price', 'Pride',
    'Prime', 'Prior', 'Prize', 'Proof', 'Proud', 'Prove', 'Psych', 'Queen', 'Queer', 'Quick',
    'Quiet', 'Quite', 'Radio', 'Raise', 'Ramen', 'Range', 'Rapid', 'Ratio', 'Reach', 'Ready',
    'Redly', 'Refer', 'Relax', 'Reply', 'Right', 'River', 'Roman', 'Rough', 'Round', 'Route',
    'Royal', 'Rugby', 'Rural', 'Sadly', 'Salve', 'Scale', 'Scene', 'Scope', 'Score', 'Secus',
    'Selly', 'Sense', 'Serve', 'Shall', 'Shape', 'Share', 'Sharp', 'Sheep', 'Sheer', 'Sheet',
    'Shift', 'Shily', 'Shirt', 'Shock', 'Shoot', 'Short', 'Shyly', 'Sight', 'Silly', 'Simon',
    'Since', 'Sixth', 'Skill', 'Skoal', 'Slash', 'Sleek', 'Sleep', 'Slyly', 'Small', 'Smart',
    'Smile', 'Smith', 'Smoke', 'Sniff', 'So-So', 'Solid', 'Solve', 'Sooey', 'Sorry', 'Sound',
    'South', 'Space', 'Spang', 'Spare', 'Speak', 'Speed', 'Spend', 'Spite', 'Split', 'Sport',
    'Squad', 'Srsly', 'Staff', 'Stage', 'Stand', 'Stark', 'Start', 'State', 'Steam', 'Steel',
    'Steep', 'Stick', 'Still', 'Stock', 'Stone', 'Store', 'Stour', 'Study', 'Stuff', 'Style',
    'Sugar', 'Super', 'Sweet', 'Table', 'Tally', 'Tanto', 'Taste', 'Teach', 'Terry', 'Thame',
    'Thank', 'Theme', 'There', 'Thiam', 'Thick', 'Thine', 'Thing', 'Think', 'Third', 'Throw',
    'Thwap', 'Tight', 'Title', 'Today', 'Tomoz', 'Total', 'Touch', 'Tough', 'Tower', 'Track',
    'Trade', 'Train', 'Treat', 'Trend', 'Trial', 'Truly', 'Trust', 'Truth', 'Twice', 'Twirp',
    'Uncle', 'Under', 'Union', 'Unity', 'Until', 'Upper', 'Upset', 'Urban', 'Usual', 'Utter',
    'Vague', 'Valid', 'Value', 'Verry', 'Video', 'Viola', 'Visit', 'Vital', 'Vivat', 'Voice',
    'Wacko', 'Wahey', 'Wanly', 'Waste', 'Watch', 'Water', 'Wetly', 'Where', 'Which', 'While',
    'Whist', 'White', 'Whole', 'Whose', 'Whoso', 'Wilma', 'Wirra', 'Woman', 'Woops', 'World',
    'Worry', 'Would', 'Wowie', 'Write', 'Wrong', 'Wryly', 'Yecch', 'Yeeha', 'Yeesh', 'Young',
    'Yours', 'Youth', 'Yowch', 'Zowie'
]

GUESSES = 10

print( '''Welcome to Coding Club Wordle

Try to guess the 5-letter secret word.

After each guess the program will tell you for each letter if it is:
    ^ in the right place
    ~ in the word, but not at this location
    x not in the word.

Have fun!
''' )

# Choose the random word to guess from WORDS (name it word).
i = random.randint(0, len(WORDS)-1)
word = WORDS[i]
# To avoid issues with the cases of letters we will standardize on using uppercase.
# Convert word to uppercase.
word = word.upper()

# print( 'Psst, the word is', word ) # For debugging only! Comment out for game play.

# Get the user's first guess (name it guess).
guess = input('What is your guess? ')
# Convert guess to uppercase.
guess = guess.upper()

# Initialize the counter of guesses to 1 (name it guesses).
guesses = 1

# Main loop: Loop while the user has not,
# - guessed the word, and
# - hasn't used up their GUESSES guesses.
while guess != word and guesses <= GUESSES:

    # Initialize the feedback string to an empty string (name it feedback).
    feedback = ''
    # Loop through the guess and the word by index (named i).
    for i in range(5):
        # If the i-th characters in guess and word are the same,
        if guess[i] == word[i]:
            # add a ^ character to feedback.
            feedback = feedback + '^'
        # Otherwise, if the i-th character in guess is in word (just not here),
        elif guess[i] in word:
            # add a ~ character to feedback,
            feedback = feedback + '~'
        # Otherwise the i-th character is not in word,
        else:
            # so add an x to feedback.
            feedback = feedback + 'x'
            
    # Display the guess and the feedback beneath it (on separate lines so they line up).
    print( guess )
    print( feedback )

    # Get the user's next guess.
    guess = input('What is your guess? ')
    # Convert guess to uppercase.
    guess = guess.upper()
    # Increment the count of guesses.
    guesses = guesses + 1

# There are two reasons the loop may have exited,
# - because they ran out of guesses, or
# - because they guessed the word.
print()

# If they guessed the word,
if guess == word:
    # Congratulate them, and
    print( 'Congratulations!' )
    # tell them how many guesses they took.
    print( 'You guessed the word in', guesses, 'guesses.' )
# Otherwise,
else:
    # Tell them they ran out of guesses,
    print( 'Sorry!' )
    print( 'You\'ve run out of guesses.')
    # and show them what the word was.
    print( 'The word was', word)
