#!/usr/bin/env python3

#Commented by: Kyle Jorgensen
#This script defines classes and functions for the dice_test.py
from random import randint #Import random integer generator

class Player: #Create basic Player class with same functions as first-oop
  def __init__(self): #tostring
    self.dice = [] #define empty list

  def roll(self): #define roll function
    self.dice = [] # clears current dice
    for i in range(3): #do 3 times:
      self.dice.append(randint(1,6)) #append to the list random value 1 - 6

  def get_dice(self): #return the list of randoms:
    return self.dice

class Cheat_Swapper(Player): #define subclass which inherits functions of Player class
  def cheat(self): #this is ONLY Cheat_Swapper's cheat function
    self.dice[-1] = 6 #this changes the final roll for Cheat_Swapper to 6 every time

class Cheat_Loaded_Dice(Player): #define subclass which inherits functions of Player class
  def cheat(self): #this is Cheat_Loaded_Dice's cheat function
    i = 0 #set variable to 0
    while i < len(self.dice): #perform the following as we iterate through items in the self.dice list
      if self.dice[i] < 6: #if the value is less than 6
        self.dice[i] += 1 #add one to the value
      i += 1 #increment the counter to the next list item
