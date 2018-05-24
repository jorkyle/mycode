#!/usr/bin/env python3

#Written by: Kyle Jorgensen
#This script will append the information from csv_users to incrementing rc files

import csv
f = open('csv_users.txt', 'r')
i = 0

##Run loop line by line:
for row in csv.reader(f):
    i += 1 #Start the counter at 1
    filename = 'admin.rc%d'%(i,) #Define output file name
    rcfile = open(filename, 'w')
    print('export OS_AUTH_URL=' + row[0], file=rcfile) #Write data from pos 0
    print('export OS_IDENTITY_API_VERSION=3', file=rcfile) #Write data from pos 1
    print('export OS_PROJECT_NAME=' + row[1], file=rcfile) #Write data from pos 2
    print('export OS_PROJECT_DOMAIN_NAME=' + row[2], file=rcfile) #Write data from pos 3
    print('export OS_USERNAME=' + row[3], file=rcfile) #Write data from pos 4
    print('export OS_USER_DOMAIN_NAME=' + row[4], file=rcfile) #Write data from pos 5
    print('export OS_PASSWORD=' + row[5], file=rcfile) #Write data from pos 6
    rcfile.close()
