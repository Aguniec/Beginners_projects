"""
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list.
"""


def first_and_last(a):
    list = [a[0], a[-1]]
    return list


a = [5, 10, 15, 20, 25]
print(first_and_last(a))
