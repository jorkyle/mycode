#!/usr/bin/env python3

#Written by: Kyle Jorgensen
#This will parse the keystone log file and detect failed logins
##The log file is included in the repo for demo purposes, but a full path can
##be used for a different file location.

loginfail = 0 #Set counter for failed logins to 0
success = 0 #Set counter for success to 0
keystone_file = open('keystone.common.wsgi', 'r')
keystone_file_lines = keystone_file.readlines()

for i in range(len(keystone_file_lines)):
    if 'Authorization failed.' in keystone_file_lines[i]: #Failure message
        loginfail += 1 #Increment the fail counter
    elif 'Loaded \d encryption keys': #If it loads successfully:
        success += 2 #Two keys per success
print('Failed login attempts: ' + str(loginfail)) #Report failures
print('Keys loaded successfully: ' + str(success)) #Report successes
