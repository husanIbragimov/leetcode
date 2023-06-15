from typing import List

"""
0 1 2 3 4 5 6 7 8 9 = index

0 1 2 3 4 5 6 7 9 = value
"""


def missingNumber(nums: List[int]) -> int:
    nums.sort()
    index = 0
    low = 0
    high = len(nums)
    while low <= high and index < high:

        if nums[low] == index:
            index += 1
            low += 1
            continue

        if nums[low] != index:
            return index

        if nums[low] <= index:
            low += 1
        elif nums[low] >= index:
            index -= 1
    return high


print(missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
