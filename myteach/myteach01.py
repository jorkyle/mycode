#!/usr/bin/env python3

#Written by: Kyle Jorgensen
#This is a simple demo of webbrowser.  It shows the capability to open a browser to
#a given address along with user-entered arguments
#Webbrowser can also be used in conjuntion with modules like BeautifulSoup
#to read links and open multiple results automatically for a given search.

import webbrowser

##Ask the user for an argument, in this case an address
addr_to_map = input('What address do you want to find on Google Maps (or Q to quit)?\n')
##Open a webpage to a URL and concatenate the user's response.
webbrowser.open('https://www.google.com/maps/place/' + addr_to_map)
