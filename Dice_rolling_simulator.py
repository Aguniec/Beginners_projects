import random

rolling = True
while rolling:
    print("Your number", random.randrange(1,6))
    print("Do you want to roll again?")
    rolling = "yes" in input()
print("Thanks for a game")

