#!/usr/bin/env python3

#Written by: Kyle Jorgensen
#This script will take an IP address...

##Ask user for an IP address
ipadd = input('Please enter an IP address or Q to quit: ')
iplist = [] #Define empty list
donotuse = 'DO NOT USE THIS ADDRESS!!! (Omitted from list)' #Message for bad values.

##Encase the whole script in while loop so you can run repeatedly and populate the list.
while True:
    if ipadd.upper() == 'Q':
        print('Thanks for playing. Goodbye.')
        break
    if ipadd == '10.10.3.1': #The first no-no address
        print(donotuse) #Blast the user with a warning message
        ipadd = input('Enter another IP or Q to quit: ')
    elif ipadd == '10.20.5.2': #The second no-no address
        print(donotuse) #Blast the user with a warning message
        ipadd = input('Enter another IP or Q to quit: ')
    else:
        iplist.append(ipadd) #Append value to previously defined list
        print('IP added. Your list now contains the following: ' + str(iplist))
        ipadd = input('Enter another IP or Q to quit: ')
