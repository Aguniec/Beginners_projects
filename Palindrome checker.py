"""
Ask the user for a string and print out whether this string is a palindrome or not.
"""


def palindrome_checker(string):
    if string[::] == string[::-1]:
        return "This is a palindrome"
    else:
        return "This is not a palindrome"


while True:
    string = input("Please eneter a word:")
    print(palindrome_checker(string))
