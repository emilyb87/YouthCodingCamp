#Lab 1
#Written By Emily Bernier
#Nov 11 2022

from math import floor


print("hello world!")

print("\"")

number=input("Enter a positive number: ")


# This IF loop calculates if a number is even or odd:
if (int(number) % 2 == 0):
    print("Even number")
else:
    print("Odd number")

#This one does the same thing, but shows the calculation:
if ((floor(int(number) / 2 ) * 2) == int(number)):
    print("Even number")
else:
    print("Odd number")
