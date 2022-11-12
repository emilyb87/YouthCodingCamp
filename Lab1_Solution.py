
numberstring=input("Enter two numbers(x,x): ")
#store two numbers in a List
numberstring=numberstring.split(",")

selection=input("Would you like to add these numbers or substract them?(A/S): ")

if (selection == "A"):
    print(int(numberstring[0]) + int(numberstring[1]))
elif (selection == "S"):
    print(int(numberstring[0]) - int(numberstring[1]))