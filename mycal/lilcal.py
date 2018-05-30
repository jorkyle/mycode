#!/usr/bin/python
import calendar


lilcal = calendar.month(2018, 1)
print("Here is a tiny calendar:")
print(lilcal)

i = 1
while i <= 12:
    print("Here is a tiny calendar:")
    print(calendar.month(2018, i))
    i += 1
current_year = input('What year is it? ')
if calendar.isleap(current_year):
    print("Replace your HDDs ASAP.")
else:
    print("Your hard drives are good for a while.")
