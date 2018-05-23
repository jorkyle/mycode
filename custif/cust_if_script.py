#!/usr/bin/env python3

#Written by: Kyle Jorgensen
#This is an if test that asks where students work.

##Ask user where they work
employer = input('What company hired you as an apprentice? ')

##Set up if statements:
if employer.lower() == 'amazon':
    print('Congratulations!  Amazon is a great place to work.')
elif employer.lower() == 'comtech':
    print('Well done! ComTech also pretty good.')
else:
    print(employer + ' is a garbage company! You\'re in the wrong room! Get out!')
print('Exiting script.') #Script finished.
