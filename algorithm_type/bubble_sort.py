import random


def bubble(nums):
    n = len(nums)
    swaps = 0
    for i in range(n - 1):
        if nums[i] > nums[i + 1]:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
            swaps += 1
    return swaps


def bubble_sort(nums):
    n = len(nums)
    for _ in range(n - 1):
        if bubble(nums) == 0:
            break


numbers = list(range(10))
random.shuffle(numbers)
print(numbers)
bubble_sort(numbers)
print(numbers)
