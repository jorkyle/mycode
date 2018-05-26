#!/usr/bin/env python3

#Written by: Kyle Jorgensen
#This will play with lists

k_file = open('snippet.txt') #Open the file
k_contents = k_file.read() #Capture file contents in variable
k_file.close() #Close the file

k_list = k_contents.split(' ') #Split file and assign to variable
print(k_list) #Test print

print('\n'.join(k_list)) #Print the join using newlines
print('\t'.join(k_list)) #Print the join using tabs
