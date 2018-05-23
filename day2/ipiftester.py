#!/usr/bin/env python3

#Written by: Kyle Jorgensen
#This script will make a list of IP addresses and report it back until user quits.

iplist = [] #Define empty list
donotuse = 'DO NOT USE THIS ADDRESS!!! (Omitted from list)' #Message for bad values.

ipadd = input('Please enter an IP address or Q to quit: ') #Ask user for IP address
##Encase the whole script in while loop so you can run repeatedly and populate the list.
while ipadd.upper() != 'Q':
    if ipadd == '10.10.3.1' or ipadd == '10.20.5.2': #The no-no addresses
        print(donotuse) #Blast the user with a warning message
        print('Your list remains: ', str(iplist))
    elif ipadd == '': #In case the user provides no input
        print('You did not provide input')
    else:
        iplist.append(ipadd) #Append value to previously defined list
        print('IP added. Your list now contains the following: ' + str(iplist))
    ipadd = input('Please enter another IP address or Q to quit: ') #Ask user for IP address
print('Thanks for playing. Goodbye.') #Farewell message
