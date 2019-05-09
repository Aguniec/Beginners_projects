""" 
Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. 
"""

number = int(input("Give me a number"))

list = list(range(1, number+1))

divisor_list = []

for i in list:
    if number % i == 0:
        divisor_list.append(i)
print(divisor_list)
