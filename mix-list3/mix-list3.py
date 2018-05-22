#!/usr/bin/env python3

#Written by: Kyle Jorgensen
#This is a list of lists, demonstrating list navigation and manipulation

##Make the list
list1 = ['cisco_nxos', 'arista_eos', 'cisco_ios']
print(list1)

##Add one item and demonstrate
list1.extend(['juniper_junos'])
print(list1)

##Append a list as another item in the original list
list1.append(['10.1.0.1', '10.2.0.1', '10.3.0.1'])
print(list1)
print(list1[4]) #Show the sub-list
print(list1[4][0]) #Show the first item in the sub list
