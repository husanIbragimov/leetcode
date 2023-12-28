from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    complements = {}

    for index, num in enumerate(nums):
        complement = target - num
        if complement in complements:
            return [complements[complement], index]
        complements[num] = index

    return []


nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))
nums = [3, 2, 4]
target = 6
print(twoSum(nums, target))
nums = [3, 5, 6, 7, 1]
target = 6
print(twoSum(nums, target))
