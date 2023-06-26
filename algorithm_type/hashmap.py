"""
Hashmap or HashTable
"""


def two_sum(arr, target: int) -> bool:
    complements = {}

    for index, num in enumerate(arr):
        complements[target - num] = index

    for index, num in enumerate(arr):
        if num in complements and complements[num] != index:
            return True

    return False


two_sum([1, 3, 5, 4, 2], 6)
print(two_sum([1, 3, 5, 4, 2], 6))
