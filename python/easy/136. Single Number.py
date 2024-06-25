from typing import List


def single_number(nums: List[int]) -> int:
    for i in range(1, len(nums)):
        nums[0] ^= nums[i]
    return nums[0]


print(single_number([4, 1, 2, 1, 2]))
# singleNumber([2, 2, 1])
