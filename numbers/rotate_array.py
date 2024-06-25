def rotate(nums: list, k: int) -> list:
    high = len(nums) - 1
    j = 0
    for i in range(len(nums)):
        if k >= j:
            nums.insert(0, nums.pop(high))
            j += 1
            print(k)
    return nums


nums = [1, 2, 3, 4]
k = 5
print(rotate(nums, k))
