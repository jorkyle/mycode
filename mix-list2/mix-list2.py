#!/usr/bin/env python3

#Written by: Kyle Jorgensen
#This program is built to demonstrate the list methods extend and append

##Set initial list values
proto = ['ssh', 'http', 'https']
protoa = ['ssh', 'http', 'https']

##Show list and demo a single value
print(proto)

##Append an item to both lists
proto.append('dns')
protoa.append('dns')
print(proto)

##Make a list of port numbers
proto2 = [22, 80, 443, 53]

########Now illustrate the difference between extend and append
##Extend proto list with proto2 contents
proto.extend(proto2)
print(proto)
##Append protoa list with proto2 contents
protoa.append(proto2)
print(protoa)
