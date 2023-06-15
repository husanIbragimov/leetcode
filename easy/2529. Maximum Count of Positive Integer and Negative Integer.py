# 2529. Maximum Count of Positive Integer and Negative Integer
from typing import List

"""
O(N) time and O(n) space
"""


def maximumCount(nums: List[int]) -> int:
    decrease = 0
    increase = 0
    for i in range(len(nums)):
        if nums[i] > 0:
            increase += 1
        elif nums[i] < 0:
            decrease += 1
    if increase > decrease:
        return increase
    return decrease


print(maximumCount([5, 20, 66, 1314]))
print(maximumCount([-2, -1, -1, 1, 2, 3]))
print(maximumCount([-3, -2, -1, 0, 0, 1, 2]))
print(maximumCount([-1764, -1562, -1226, -1216, -402, -386, -133, 979, 1227, 1992]))
