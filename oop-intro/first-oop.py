#!/usr/bin/env python3

#Written by: Kyle Jorgensen
#This is a simple dice game

from random import randint #Import random int generator

class Player: #Set up the class
    def __init__(self): #toString
        self.dice = [] #define empty list

    def roll(self): #define the roll function
        self.dice = [] #reset the list
        for i in range(3): #Roll three times
            self.dice.append(randint(1,6)) #Choose an int between 1 and 6 and append to list self.dice

    def get_dice(self): #this method simply returns the results
        return self.dice

player1 = Player() #set player1 as Player class object
player2 = Player() #set player2 as Player class object

player1.roll() #roll player1
player2.roll() #roll player2

print('Player 1 rolled ' + str(player1.get_dice())) #print list results
print('Player 2 rolled ' + str(player2.get_dice()))

if sum(player1.get_dice()) == sum(player2.get_dice()): #If sums are same
    print('Draw!')
elif sum(player1.get_dice()) > sum(player2.get_dice()): #If player1 sum is more
    print('Player 1 wins!')
else: #If player2 sum is more
    print('Player 2 wins!')
