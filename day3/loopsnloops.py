#!/usr/bin/env python3

#Written by: Kyle Jorgensen
#This program will execute a loop to report hypothetical switch attributes.

##Define switch attributes
cisco_ios = {'device_type': 'cisco_ios_ssh', 'ip': '10.10.10.27', 'username': 'admin', 'password': 'passwd', 'port': 22}

##Make the 'for' loop to print the info for each value in the dictionary.
for x in cisco_ios.values():
    print('CISCO LOGIN INFO - ' + str(x)) #Use string output for x
print('Exiting script.  Have a nice day.') #Notify user of exit
