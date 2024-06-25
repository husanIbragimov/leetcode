# 35. Search Insert Position

def search_insert_position(nums, target) -> int:
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    if nums[left] < target:
        return left + 1
    return left


numbers = [1, 3, 5, 6]
tar = 7

# answer: 4
# index:  0  1  2  3       0  1  2  3  4
# list:  [1, 3, 5, 6] --> [1, 3, 5, 6] 7
# bor sonni index ini aniqlaydi, yo'q bo'lganni esa bor bo'lganda qaysi indexda bo'lishi mumkinligini aniqlash


# print(search_insert_position(numbers, tar))
