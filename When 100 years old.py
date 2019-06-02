""" Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they will turn 100 years old. """

import datetime


def when_100_years_old():
    now = datetime.datetime.now()
    name = input("What's your name? \n")
    age = int(input("Okay {}, how old are you?\n".format(name.title())))

    years = (now.year + 100) - age
    when = "{}, so if you are {} now then you should turn 100 in the year {}".format(
        name.title(), age, years)
    return when


print(when_100_years_old())
