"""
Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. 
The passwords should be random, generating a new password every time the user asks for a new password. 
Include your run-time code in a main method.

"""
import random
import string

how_many = int(input("How many symbols do you want?"))


def password_generator(how_many):

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    everything = lowercase + uppercase + digits + special
    password = random.sample(everything, how_many)

    for i in password:
        password = "".join(password)
    return (password)

password = password_generator(how_many)
print(password)
