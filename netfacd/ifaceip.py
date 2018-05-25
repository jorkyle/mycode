#!/usr/bin/env python3

#Written by: Kyle Jorgensen
#Defines a function to poll the user for an interface and reports IP

import netifaces #Import netifaces module

ifaces = netifaces.interfaces() #set variable for easier reading
print(ifaces) #Show options for valid interface options
ifaceip = input('What interface would you like to see?\n') #Ask the user.

def showifaceip(ifaces): #Define the function
    if ifaceip in ifaces: #If the input matches an item in netifaces.interfaces()
        try: #Use 'try' because if there is no stored value, the program breaks.
            print(netifaces.ifaddresses(ifaceip)[netifaces.AF_INET][0]['addr'])
        except: #If there is no stored value, the function will spit this out instead of an error.
            print('No address assigned.')
    else: #If the input does not match an item in netifaces.interfaces()
        print('That is not a valid interface.')

showifaceip(ifaces) #Run the function
