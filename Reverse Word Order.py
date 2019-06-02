"""
Write a program that asks the user for a long string containing multiple words. 
Print back to the user the same string, except with the words in backwards order.
"""


def reverse_order(string):

    words_to_array = string.split()
    reverse_words_order = a[::-1]
    return " ".join(reverse_words_order)


string = input("Give me a word")
print(reverse_order(string))
