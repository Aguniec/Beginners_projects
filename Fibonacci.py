"""
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
"""

number = int(input("Give me a number"))

list_of_numbers = [0,1]

for i in range (0, number):
    a = list_of_numbers[-1] + list_of_numbers[-2]
    list_of_numbers.append(a)

print(list_of_numbers)

