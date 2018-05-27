#!/usr/bin/env python3

#Edited by: Kyle Jorgensen
#This program runs through a user-defined number of dice rounds.

from cheatdice import * #import everything from cheatdice
swapper = Cheat_Swapper() #set object swapper as Class Cheat_Swapper
loaded_dice = Cheat_Loaded_Dice() #set object loaded_dice as Class Cheat_Loaded_Dice
swapper_score = 0 #set scores to 0
loaded_dice_score = 0
tie_games = 0 #added tie games because I thought it relevant
number_of_games = int(input('How many rounds shall we run this time? ')) #ask user how many rounds, int required
game_number = 0 #start game counter at 0
print("Simulation running")
print("==================")
while game_number < number_of_games: #run loop until game number hits the user-defined number
  swapper.roll() #run roll functions for each player
  loaded_dice.roll()

  swapper.cheat() #apply each player's cheat function to their rolled numbers
  loaded_dice.cheat()
   #Remove # before print statements to see simulation running
   #Simulation takes approximately one hour to run with print <-- lololol one hour? On what hardware?
   #statements or ten seconds with print statements
   #commented out

#print("Cheater 1 rolled" + str(swapper.get_dice()))
#print("Cheater 2 rolled" + str(loaded_dice.get_dice()))
  #print(str(game_number)) <-- added this for troubleshooting
  if sum(swapper.get_dice()) == sum(loaded_dice.get_dice()): #if they tie
    #print("Draw!")
    tie_games += 1 #increment tie_games counter
  elif sum(swapper.get_dice()) > sum(loaded_dice.get_dice()): #if swapper wins
    #print("Dice swapper wins!")
    swapper_score+= 1 #increment swapper_score
  else: #if loaded_dice wins
    #print("Loaded dice wins!")
    loaded_dice_score += 1 #increment loaded_dice_score
  game_number += 1 #increment game number at end of loop

##When it's all done, print the overview for the user:
print("Simulation complete") #
print("-------------------")
print("Final scores")
print("------------")
print("Swapper won: " + str(swapper_score)) #score needs to be string to concatenate
print("Loaded dice won: " + str(loaded_dice_score))
print("Rounds tied: " + str(tie_games))
if swapper_score == loaded_dice_score: #if final totals are the same
  print("Game was drawn")
elif swapper_score > loaded_dice_score: #if final totals favor swapper
  print("Swapper won most games")
else: #if final totals favor loaded_dice
  print("Loaded dice won most games")
