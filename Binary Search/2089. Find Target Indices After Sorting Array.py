from typing import List


def targetIndices(nums: List[int], target: int) -> List[int]:
    nums.sort()
    # print(nums)
    low = 0
    high = len(nums)
    result = []
    while low < high:
        guess = nums[low]
        if guess == target:
            result.append(low)
        low += 1

    return result


print(targetIndices([1, 2, 5, 2, 3], 2))
