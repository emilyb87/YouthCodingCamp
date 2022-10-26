# trivia.py

print('Trivia Generator')
print('----------------')

# Input
print('What is your name?')
name = input()

print('Hi', name, ' I have some questions for you:')
print('How old are you?')
age = input()
age = int(age)

print('How much do you weigh? (in pounds)')
weight = input()
weight = int(weight)

# Processing
dog_years = age * 7
moon_weight = weight / 6
sun_weight = weight * 27.9

# Output
print('You are', dog_years, 'years old in dog-years.')
print('On the moon you would only weigh', moon_weight, 'pounds.')
print('While on the sun you would weigh', sun_weight, 'pounds (but not for long!).')

