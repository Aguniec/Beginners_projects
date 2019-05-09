""" Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they will turn 100 years old.
Add on to the previous program by asking the user for another number and printing out that many copies of the previous message.
Print out that many copies of the previous message on separate lines. """

import datetime

now = datetime.datetime.now()

name = input("What's your name? \n")
age = int(input("Okay {}, how old are you?\n".format(name.title())))

years = (now.year + 100) - age
when = "{}, so if you are {} now then you should turn 100 in the year {}".format(name.title(),age,years)
print(when)

n = int(input("Okay {}, give me a number \n".format(name)))

when += "\n"
print (when * n)
