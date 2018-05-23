#!/usr/bin/env python3

#Written by: Kyle Jorgensen
#This is a program to perform Lab 16, which is something to do with Monty Python

round = 0 #Set round increment to 0
print('Finish the movie title:') #Ask the question here so it doesn't repeat unnecessarily.
print('Monty Python\'s The Life of _____') #State the movie
while True: #Start the while loop
    round += 1 #Increment by 1 the round.
    answer = input() #Capture the user input
    if answer.lower() == 'brian': #The correct answer
        print('Correct!')
        break #Game over. You win.
    elif answer.lower() == 'shrubbery': #The secret answer
        print('You found the super secret answer!  Way to go!')
        break #Game over. You win extra.
    else:
        print('Nope! Try again!') #Wrong answer.  Keep trying until correct.
