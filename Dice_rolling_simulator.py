import random


def rolling():
    rolling = True
    while rolling:
        print("Your number is ", random.randrange(1,6))
        print("Do you want to roll again?")
        rolling = ("yes" or "y") in input().lower()
    print("Thanks for a game")


rolling()

