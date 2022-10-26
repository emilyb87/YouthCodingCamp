# sqrt.py
#
# Find the square estimate of a number using Newton's Method.

print(18*'√')
print('Square root finder')
print(18*'√')
num = float(input( 'What number would you like me to find the square root of: ' ))
estimate = num / 2
# print( estimate )
revised_estimate = 0.5 * (estimate + num / estimate)
while abs(estimate - revised_estimate) > 0.0000000001:
    estimate = revised_estimate
    revised_estimate = 0.5 * (estimate + num / estimate)
    # print( revised_estimate )
print( 'I estimate the square root of', num, 'to be', revised_estimate)
