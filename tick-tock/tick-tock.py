#!/usr/bin/env python3
import time # This is required to include time module

def calculate_age(born):
    today = time.localtime(ticks)

## Count the number of ticks from the epoch
ticks = time.time()
print("Number of ticks since 12:00am, January 1, 1970: " + str(ticks))

## Show how we can convert ticks into a useful time tuple
myTime = time.localtime(ticks) # pass ticks to localtime
print("The local time touple is: " + str(myTime))
print("The local time touple year is: " + str(myTime[0]))
print("The local time touple month is: " + str(myTime[1]))
print("The local time touple day is: " + str(myTime[2]))
print("The local time touple hour is: " + str(myTime[3]))
print("The local time touple minute is: " + str(myTime[4]))
print("The local time touple second is: " + str(myTime[5]))
print("The local time touple week is: " + str(myTime[6]))
print("The local time touple year is: " + str(myTime[7]))
print("The local time touple daylight savings is: " + str(myTime[8]))

print("Your date of birth (dd mm yyyy):\n")
bday, bmonth, byear = input("--->").split()


def calculate_age(bday, bmonth, byear):
    today = time.localtime(ticks)
    return today[0] - byear - ((today[1], today[2]) < (bmonth, bday))

def age_seconds(born):
    today = time.localtime(ticks)
    return ticks - time.gmtime('%d%m%Y%H%M%S', bday,bmonth,byear,'00','00','00')
age = calculate_age(int(bday), int(bmonth), int(byear))

print(age)

future_500 = int(ticks) + 500

print('500 seconds from now: ' + str(future_500) + '\n' + time.strftime('%H%M', time.localtime(future_500)))
