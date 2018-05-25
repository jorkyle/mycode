#!/usr/bin/env python3

#Code from: Lab 28, Edited by Kyle Jorgensen
#This program reports network interface information

import netifaces #Import netifaces module

print(netifaces.interfaces()) #Print interfaces

for i in netifaces.interfaces(): #For each item in the netifaces.interfaces() list
    print('\n****** details of interface - ' + i + ' ******') #Print a delineation
    try: #Use try because some items will be missing values.
        print('MAC: ', end='') # This print statement will always print MAC without an end of line
        print((netifaces.ifaddresses(i)[netifaces.AF_LINK])[0]['addr']) # Prints the MAC address
        print('IP: ', end='')  # This print statement will always print IP without an end of line
        print((netifaces.ifaddresses(i)[netifaces.AF_INET])[0]['addr']) # Prints the IP address
    except:          # This is a new line
        print('Could not collect adapter information') # Print an error message
