"""
Ask the user for a number and determine whether the number is prime or not

"""

number = int(input("Give me a number"))

list = list(range(1, number + 1))

divisor_list = []

for i in list:
    if number % i == 0:
        divisor_list.append(i)

if divisor_list.__len__() == 2:
    if 1 in divisor_list and number in divisor_list:
        print('prime')
else:
    print("not prime")
