"""
Linear Search
"""


def linear_search(arr, item):
    i = 0
    for n in range(len(arr)):
        i = i + 1
        if arr[n] == item:
            return f'n: {n}; i: {i};'
    return None


my_arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
my_item = 10
print(linear_search(my_arr, my_item))
