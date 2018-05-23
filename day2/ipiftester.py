#!/usr/bin/env python3

#Written by: Kyle Jorgensen
#This script will take an IP address...

iplist = [] #Define empty list
donotuse = 'DO NOT USE THIS ADDRESS!!! (Omitted from list)' #Message for bad values.

##Encase the whole script in while loop so you can run repeatedly and populate the list.
while True:
    ipadd = input('Please enter an IP address or Q to quit: ') #Ask user for IP address
    if ipadd.upper() == 'Q':
        print('Thanks for playing. Goodbye.')
        break
    if ipadd == '10.10.3.1' or ipadd == '10.20.5.2': #The no-no addresses
        print(donotuse) #Blast the user with a warning message
        print('Your list remains: ', str(iplist))
    else:
        iplist.append(ipadd) #Append value to previously defined list
        print('IP added. Your list now contains the following: ' + str(iplist))
