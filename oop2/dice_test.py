#!/usr/bin/env python3

#Commented by: Kyle Jorgensen
#This dice sim imports classes from another file

from cheatdice import Player #Import necessary classes
from cheatdice import Cheat_Swapper #Import necessary classes
from cheatdice import Cheat_Loaded_Dice #Import necessary classes

cheater1 = Cheat_Swapper() #This is the one who rolls 6 on roll 3 every time.
cheater2 = Cheat_Loaded_Dice() #This is the one who adds 1 to every value (except 6)

cheater1.roll() #Players roll their random numbers as normal
cheater2.roll()

cheater1.cheat() #Call cheat function to work some magic on those random ints
cheater2.cheat() #Call cheat function to work some magic on those random ints

print("Cheater 1 rolled" + str(cheater1.get_dice())) #Report results
print("Cheater 2 rolled" + str(cheater2.get_dice()))

if sum(cheater1.get_dice()) == sum(cheater2.get_dice()): #If sums are the same:
  print("Draw!")

elif sum(cheater1.get_dice()) > sum(cheater2.get_dice()): #If cheater1 sum is higher:
  print("Cheater 1 wins!")

else: #If cheater2 sum is higher:
  print("Cheater 2 wins!")
