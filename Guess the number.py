"""
Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
"""

import random


def guess_the_number():

    r = random.randint(1, 9)
    user_input = input("Please guess the number:")
    if user_input == "exit":
        quit()
    if int(user_input) == r:
        message = "Congrats!, Do you want to play again? If no, type 'exit'"
    elif r > int(user_input):
        message = "The number is too small, please guess again"
    elif r < int(user_input):
        message = "The number is too large, please guess again"
    else:
        message = "Inncorect command"
    return message


while True:
    print(guess_the_number())
