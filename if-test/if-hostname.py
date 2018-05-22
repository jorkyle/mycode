#!/usr/bin/env python3

#Written by: Kyle Jorgensen
#This is the first 'if' test lab

##Ask user to set the hostname
hostname = input('What is your hostname? ')

##Set conditional 'if' statement.
if hostname.upper() == 'MTG':
    print('The hostname was found to be some variant of mtg.')
    print('hostname matches expected config')
print('Exiting the script.') #Notify user of exit.
