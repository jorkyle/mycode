#!/usr/bin/env python3

#Written by: Kyle Jorgensen
#This script calculates factorials for a user-selected number.

x = int(input('Please enter a number: ')) #Poll user for a number
f = 1 #Declare f as variable
for i in range(1, x+1): #Set the range for the loop
    f = f * i #run the calculation
print(str(x) + '! = ' + str(f)) #Report the calculation
