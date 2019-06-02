""" Take a list, say for example this one: a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
Ask the user for a number and return a list that contains only elements from the original list a that 
are smaller than that number given by the user."""


def only_small_numbers(number, array):
    smaller_number_list = [i for i in array if number > i]
    return smaller_number_list


array = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
number = int(input("Choose a number:"))
print(only_small_numbers(number, array))
