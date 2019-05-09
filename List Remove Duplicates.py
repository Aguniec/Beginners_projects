"""
Write a program that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
"""

a = [1,1,2,2,3,3]
b = set()
for i in range (0,len(a)):
        b.add(a[i])
print (b)

for i in range (0, len(a)):
    if a[i] not in b:
        b.append(a[i])
print(b)

