#!/usr/bin/env python3

#Written by: Kyle Jorgensen
#This will grab an IP from file and run the associated commands

import socket #Import module to work with and recognize IP addresses

ipcmdfile = open('ipcmd.txt') #Open the file containing IPs and associated commands
readfile = ipcmdfile.readlines() #Read the contents and save as a list
ipcmdfile.close() #Close the file; we're done with it.

def pushcommand(address): #Define the function
    for i in readfile: #For each line
        try:
            socket.inet_aton(i) #Test to see if the line contains an IP address
            print(i, end='') #Print the IP for the user
        except:
            print('Pushing command: ' + i, end='') #Take non-IP values and report the command being simulated

pushcommand(readfile) #Run it to test.
