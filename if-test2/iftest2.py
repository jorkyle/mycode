#!/usr/bin/env python3

#Written by: Kyle Jorgensen
#This is iftest 2

ipchk = input('Apply an IP address: ') #Prompt the user for input

if ipchk == '192.168.70.1': #This is a bad choice, so we'll tell the user.
    print('Looks like the IP address of the gateway was set to: ' + ipchk + ' This is not recommended.')
elif ipchk: #Anything else, valid or not, is okay with us.
    print('Looks like the IP address of the gateway was set to: ' + ipchk + '. Success.')
else: #Tell the user if no input is received.
    print('You did not provide input.')
print('Exiting script.') #Notify user of exit.
