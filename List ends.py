"""
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list.
"""

a = [5, 10, 15, 20, 25]

def first_and_last(a):
    list = [a[0], a[-1]]
    return list

x = first_and_last(a)
print(x)
