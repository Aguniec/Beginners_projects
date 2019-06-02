"""
Ask the user for a number and determine whether the number is prime or not

"""


def is_prime():
    number = int(input("Give me a number"))
    numbers_list = list(range(1, number + 1))
    divisor_list = [i for i in numbers_list if number % i == 0]
    if len(divisor_list) == 2:
        message = "Number is prime"
    else:
        message = "Number is not prime"
    return message


print(is_prime())
