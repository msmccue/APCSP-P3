#Mike McCue

#TODO: randomly generate a number (in a certain range) - DONE
#TODO: ask the user for a guess - DONE
#TODO: compare the guess to random number; if too low, display "too low" - DONE
#TODO: ask for a guess again [until they are correct]
#TODO: repeat until user does not want to play again

import random

#CITE: found random on geeksforgeeks
#the equals sign is an assignment operator
randNum = random.randrange(1,10)

#debugging
print(randNum)

value = int(input("Guess a number (1-10):"))

#debugging
print(value)

if (value < randNum):
    print("Too low!")

if (value > randNum):
    print("Too high!")

if (value == randNum):
    print("Good job!")
    
