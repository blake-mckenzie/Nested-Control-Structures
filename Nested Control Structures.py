'''
Programmer: Blake McKenzie
Date: 10.15.19
Program: Double For Loop

This program will nest a For Loop
inside of another For Loop
'''


#This program will have both an inner and outer for loop

for i in range (3):
    print ("Outer For Loop: " + str(i))
    for l in range (2):
        print ("     Inner For Loop: " + str(l))



print ("\n****************\n")


'''
Programmer: Blake McKenzie
Date: 10.23.19
Program: Categories
This program will ask users for an interest of them
then ask for two items related to that interest
'''
for i in range(4): 
    print ("Outer For Loop: " + str(i)) 
    x = 6 
    while x >= 0:
        print("    While Loop: " + str(x))
        x = x - 1
