"""
Ask the user for a string and print out whether this string is a palindrome or not.
"""

string = str(input("Please eneter a word:"))

if string[::]==string[::-1]:
    print("This is a palindrome")
else:
    print("This is not a palindrome")
