#!/usr/bin/env python3

#Written by: Kyle Jorgensen
#This program will tell the user whether or not a L2 protocol is allowed.

while True:
    print('Please enter a Layer 2 network protocol or press \'Q\' to quit.') #Prompt user for L2 protocol
    var1 = input() #Assign user input to var1
    if var1.lower() == 'q': #If they press 'q' then quit
        print('Program ending.  Thanks for playing.')
        break #Quit the loop
    ## The following conditions each have their own custom message.
    if var1.lower() == 'eth':
        print('Ethernet protocol allowed')
    elif var1.lower() == 'fc':
        print('Fibre Channel NOT allowed')
    elif var1.lower() == 'ifb':
        print('Infiniband NOT allowed')
    elif var1.lower() == 'otn':
        print('Optical Network allowed')
    else:
        print('No idea what that technology is')
