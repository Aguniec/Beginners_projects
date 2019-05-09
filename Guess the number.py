"""
Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
"""

import random

r = random.randint(1, 9)

while True:
    guess = input("Please guess the number:")
    if guess.lower().__contains__('exit'):
        break
    else:
        try:
            x = int(guess)
            if x == r:
                print("Congrats!, Do you want to play again?")
            elif r > x:
                print("The number is too small, please guess again")
            elif r < x:
                print("The number is too large, please guess again")
        except:
            print("this is not a number")
