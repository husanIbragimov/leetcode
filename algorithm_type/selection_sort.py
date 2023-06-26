def select(nums, start):
    n = len(nums)
    pos = start
    for i in range(start, n):
        if nums[i] < nums[pos]:
            pos = i
    return pos


nums = [8, 3, 4, 2, 7, 6, 1, 5, 9]
print(select(nums, 0))
print(nums[5])


def selection_sort(nums):
    n = len(nums)
    for i in range(n):
        pos = select(nums, i)
        nums[pos], nums[i] = nums[i], nums[pos]
        print(nums)


selection_sort(nums)

# index = 6: value = 1
# [1, 3, 4, 2, 7, 6, 8, 5, 9]
# [1, 2, 4, 3, 7, 6, 8, 5, 9]
# [1, 2, 3, 4, 7, 6, 8, 5, 9]
# [1, 2, 3, 4, 7, 6, 8, 5, 9]
# [1, 2, 3, 4, 5, 6, 8, 7, 9]
# [1, 2, 3, 4, 5, 6, 8, 7, 9]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
