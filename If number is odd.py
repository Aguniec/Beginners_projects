""" Ask the user for a number. 
Depending on whether the number is even or odd, print out an appropriate message to the user.
If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
If check divides evenly into num, tell that to the user. If not, print a different appropriate message."""


def if_number_is_odd(n):

    if n > 4 and n % 4 == 0:
        message = "Your number is a multiple of 4"
    elif n % 2 == 0:
        message = "Your number is not odd"
    else:
        message = "Your number is odd"
    return message


def if_number_is_devided(n, div):
    if n % div == 0:
        message = "{0}, devides by, {1}".format(n, div)
    else:
        message = "{} does not divide by {}".format(n, div)
    return message


n = int(input("Give me a number to check:"))
div = int(input("Give me a number to divide by:"))
print("Your check number is {} and divisor is {}".format(n, div))

print(if_number_is_odd(n), if_number_is_devided(n, div))
