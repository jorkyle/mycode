#!/usr/bin/env python3

#Written by: Kyle Jorgensen
#This program will simulate reservation of a block of IP addresses, 10 at a time

print('Hello. This program reserves a block of IP addresses, 10 at a time.')
k_ip_addr = input('What is your starting IP? ') #Accept a string input (IPv4 address) from a user
k_ip_range = input('How many addresses would you like to reserve? ')

k_ip_split = k_ip_addr.split('.') #1) Remove the dot notation with .split()
##Taking the range-1 approach yields accurate results since the reported list will be inclusive
##eg: User wants 1 address but the math would do 1+1. 1-11 is 11 values, not 10.
k_ip_last = int(k_ip_split[3]) + int(k_ip_range) - 1 #2) Add range to the final item in the list

def ip_ranger(ip): #Define the function
    if k_ip_last >= 255: #Include 255 since it's not a valid host address
        print('Address out of range.') #Tell the user it's no good
        return False
    else:
        print('Address range accepted (' + k_ip_addr + '-' + str(k_ip_last) + ')') #Tell user it's good and what addresses are to be used
        return True

ip_ranger(k_ip_addr) #Run it!
