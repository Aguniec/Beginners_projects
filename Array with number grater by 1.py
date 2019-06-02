"""Make a function that take an array of the numbers representing a number and output an array
that contains values of the first number grater by 1"""


def make_number(array):
    count = 1
    reverse_sorted = array[::-1]
    sum = 0
    for i in reverse_sorted:
        sum += i * (count)
        count = count * 10
    second_number = sum + 1
    second_array = [int(i) for i in str(second_number)]
    return second_array


print(make_number([1, 3, 2, 4, 9]))
