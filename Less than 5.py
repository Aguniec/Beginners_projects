""" Take a list, say for example this one: a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.
Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this 
list in it and print out this new list.
Ask the user for a number and return a list that contains only elements from the original list a that 
are smaller than that number given by the user."""


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  
#Make a new list that has all the elements less than 5
new_list = []
for i in a:
    if i < 5:
        new_list.append(i)
print(new_list)

#Make a list that contains only numbers less than number given by user
number = int(input("Choose a number:"))
new_list = []
for i in a:
    if i < number:
        new_list.append(i)
print(new_list)

