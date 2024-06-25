def moveZeroes(nums):
    last_zero_index = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[last_zero_index], nums[i] = nums[i], nums[last_zero_index]
            last_zero_index += 1
    return nums


#       0  1  2  3  4  5  6  7  8
nums = [4, 8, 0, 0, 0, 1, 0, 3]
print(nums, "current")
print(print(moveZeroes(nums)))
