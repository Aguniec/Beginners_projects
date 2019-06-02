"""
Write a program that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
"""


def remove_dupliactes(a):
    return list(set(a))


a = [1, 1, 2, 2, 3, 3]
print(remove_dupliactes(a))
