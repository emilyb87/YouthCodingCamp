#Iteration, while, ifs, for

#For and while loops are used to make loops of repeating series
#For example, let's say we want to count to ten:
#Lets create a list:
ten=[0]
#We won't put all 10 numbers in this list, because we can do it in the for loop:
for i in ten:
    print(ten[i]) #i is the position in the list
    #then, we add i every iteration. The first number being the position in the list, the second is ADDING to the list
    ten.insert(i+1, i+1)
    #This will cause an infinite loop. Let's stop the loop after 10:
    if i==10:
        break;
print("for ----------------")

#But we could also just use range()
for i in range(11):
    print(i)
#this gives the same result
print("range----------------")

#How about with a while loop?
i=0
while(i<10):
    print(i)
    #If you don't increment i, the loop will go on forever.
    i+=1

print("while 1----------------")
#Continue: with continue, you can skip iterations
i=0
while(i<10):
    i+=1
    if(i==3): #this will skip the 3
       continue
    print(i)

print("while 2----------------")