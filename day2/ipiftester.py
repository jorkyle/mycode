#!/usr/bin/env python3

#Written by: Kyle Jorgensen
#This script will take an IP address...

##Ask user for an IP address
ipadd = input('Please enter an IP address: ')
iplist = [] #Define empty list
donotuse = 'DO NOT USE THIS ADDRESS!!! (Omitted from list)' #Message for bad values.

##Encase the whole script in while loop so you can run repeatedly and populate the list.
while True:
    if ipadd == '10.10.3.1': #The first no-no address
        print(donotuse) #Blast the user with a warning message
    elif ipadd == '10.20.5.2':n #The second no-no address
        print(donotuse) #Blast the user with a warning message
    else:
        iplist.append(ipadd) #Append value to previously defined list
        print('IP added. Your list now contains the following: ' + str(iplist))
    answer = input('Run again? (y/n) ') #Prompt user to keep going or not
    if answer == 'y':
        ipadd = input('Please enter another IP address: ') #Get another value
        continue #Start again with while loop
    else:
        print('Goodbye') #Confirm exit
        break #End the loop
