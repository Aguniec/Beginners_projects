"""

Take two lists, say for example these two: a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], 
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). 
Make sure your program works on two lists of different sizes.
"""


import random

# Only common elements in one list
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

new_list = []

for i in a:
    if i in b:
        if i not in new_list:
            new_list.append(i)
print(new_list)

# List with random numbers
c = []
d = []

for i in range(0, 50):
    x = random.randint(1, 10)
    y = random.randint(8, 18)
    c.append(x)
    d.append(y)

print(c, d)

new_list = []

for i in c:
    if i in d:
        if i not in new_list:
            new_list.append(i)
print(new_list)
