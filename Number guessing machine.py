
from random import randint
number = (randint (1, 100))
guess = 0

print ("Welcome to the Amazing Number Guessing Machine")

print ("")

print ("I have chosen a positive integer between 1 and 100")
                 
while True:
    try:
        userinput = input ("What is you guess? ")
        userinput = int (userinput)
        if userinput>number:
                print (" Guess is too high, try again")
                guess = guess+1
        if userinput<number:
                print ("Guess is too low, try again")
                guess = guess+1
        if userinput==number:
                guess = guess+1
                print ("You guessed it in" ,guess, "trys")
                
                break
    except:
        print ("Invalid Int, Try Again")
        guess = guess+1
