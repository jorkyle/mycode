#!/usr/bin/env python3

#Written by: Kyle Jorgensen
#This will parse the keystone log file and detect failed logins
##The log file is included in the repo for demo purposes, but a full path can
##be used for a different file location.

loginfail = 0 #Set counter for failed logins to 0
success = 0 #Set counter for success to 0
keystone_file = open('keystone.common.wsgi', 'r')
keystone_file_lines = keystone_file.readlines()
keystone_file.close() #Close the file. We're done since the lines have been read into a variable.

for i in range(len(keystone_file_lines)):
    if 'Authorization failed.' in keystone_file_lines[i]: #Failure message
        loginfail += 1 #Increment the fail counter
        ###Record the IP address by splitting the line and reporting the last item:
        print('Line ' + str(i) + ': Failure recorded from: ' + keystone_file_lines[i].split()[-1])
    elif 'Loaded 2 encryption keys': #If it loads successfully:
        success += 2 #Two keys per success
print('Failed login attempts: ' + str(loginfail)) #Report failures
print('Keys loaded successfully: ' + str(success)) #Report successes
