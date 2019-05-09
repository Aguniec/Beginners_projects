"""
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
"""

number = int(input("Give me a number"))

list = [0,1]

for i in range (0,number):
    a = list[-1] + list [-2]
    list.append(a)

print(list)

