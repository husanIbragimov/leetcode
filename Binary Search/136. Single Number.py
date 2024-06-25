from typing import List

# 136. Single Number
"""
    Massivda juft sonlar berilgan qaysi biridiningdir jufti yo'q, Yolg'iz qolgan sonni topish kerak
    [ 2, 2, 3, 3, 4, 5, 5, 4, 1]
    result = 1
    
    Processing...

"""


def singleNumber(nums: List[int]) -> int:
    nums.sort()
    low = 0
    high = len(nums) - 1
    # while low < high:
    #     if nums[low] != nums[high]:
    #         return nums[high]
    #     low += 1
    #     high -= 1
    #     return 1
    for i in range(len(nums)):
        for j in range(len(nums)-i):
            if nums[j] != nums[i]:
                return nums[j]


print(singleNumber([4, 1, 2, 1, 2]))
# print(singleNumber([2, 2, 1]))
# print(singleNumber([2, 2, 3, 3, 4, 5, 5, 4, 1]))
