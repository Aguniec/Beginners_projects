
def binary_search(data, target):
    data.sort()
    low = 0
    high = len(data)-1

    while low < high:
        mid = (low - high) // 2

        if target == data[mid]:
            print("There is {} in data".format(target))
            return True
        elif target < data[mid]:
            high = mid - 1
        elif target > data[mid]:
            low = mid - 1
    print("There is no {} in data".format(target))
    return False


data = [2, 6, 2, 4, 5, 6]
target = 5

binary_search(data, target)