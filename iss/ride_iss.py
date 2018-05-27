#!/usr/bin/env python3

#Edited by: Kyle Jorgensen
#This will pull JSON from a site containing all current astronauts in space,
#convert it to a python dictionary, and report it in readable form

import urllib.request #import url request function
import json #import JSON reader
## Trace the ISS
majortom = 'http://api.open-notify.org/astros.json' #set variable to the URL

## Call the webservice
groundctrl = urllib.request.urlopen(majortom)

## put fileobject into helmet
helmet = groundctrl.read()

## decode json to python data structure
helmetson = json.loads(helmet.decode('utf-8'))

## display our pythonic data
#print("\n\nConverted python data")
#print(helmetson)

print("People in Space: ", helmetson['number']) #print the number of people
people = helmetson['people']
#print(people)

for i in people: #make a loop to print values from name/craft keys
    print(i['name'] + ' on the ' + i['craft'])
