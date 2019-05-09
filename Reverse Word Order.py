"""
Write a program that asks the user for a long string containing multiple words. 
Print back to the user the same string, except with the words in backwards order.
"""

def function():
    word = input("Give me a word")
    a = word.split()
    b = a[::-1]
    c = " ".join(b)
    print(c)
function()
