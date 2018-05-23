#!/usr/bin/env python3

#Written by: Kyle Jorgensen
#This is a program to perform Lab 16, which is something to do with Monty Python

round = 0
print('Finish the movie title:')
print('Monty Python\'s The Life of _____')
while True:
    round += 1
    answer = input()
    if answer.lower() == 'brian':
        print('Correct!')
        break
    elif answer.lower() == 'shrubbery':
        print('You found the super secret answer!  Way to go!')
        break
    else:
        print('Nope! Try again!')
