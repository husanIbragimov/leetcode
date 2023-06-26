"""
Binary Search
"""
from typing import List


def binary_search(arr, item):
    low = 0
    high = len(arr) - 1
    i = 0
    while low < high:
        i = i + 1
        mid = (low + high) // 2
        guess = arr[mid]
        if guess < item:
            low = mid + 1
        else:
            high = mid - 1
        if guess == item:
            return f"mid: {mid}, i: {i}"
    return None


my_arr = [-1, 0, 3, 5, 9, 12]
my_item = 9


# print(binary_search(my_arr, my_item))

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


# 852. Peak Index in a Mountain Array

def peak_index_in_mountain_array(arr) -> int:
    low = 0
    high = len(arr) - 1
    while low < high:
        mid = (low + high) // 2
        if arr[mid] < arr[mid + 1]:
            low = mid + 1
        else:
            high = mid
    return low


mountain = [0, 10, 5, 2]


# print(peak_index_in_mountain_array(mountain))


# answer: 1
# har bir to'g'ri qadam uchun +1


# 367. Valid Perfect Square

def is_perfect_square(num: int) -> bool:
    low = 1
    high = num

    while low <= high:
        mid = (low + high) // 2
        sq = mid ** 2

        if num == sq:
            return True
        if sq < num:
            low = mid + 1
        elif sq > num:
            high = mid - 1

    return False


value = 16


# print(is_perfect_square(value))
# math.sqrt(16) --> True

# 2089. Find Target Indices After Sorting Array

def targetIndices(nums, target: int):
    nums.sort()
    print(nums)
    low = 0
    high = len(nums) - 1
    result = []
    while low < high:
        mid = (low + high) // 2
        if nums[mid] < target:
            result.append(nums[low])
            low = mid + 1

    return result


# print(targetIndices([1, 2, 5, 2, 3], 4))


# 704. Binary Search

def search(nums, target) -> int:
    low = 0
    high = len(nums) - 1
    while low <= high:
        if len(nums) < 2:
            return 0
        mid = (low + high) // 2
        guess = nums[mid]
        if guess < target:
            low = mid + 1
        else:
            high = mid - 1

        if guess == target:
            return mid

    return -1


# print(search([9], -9))

# 349. Intersection of Two Arrays

def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    nums1.sort()
    nums2.sort()
    i = j = 0
    n, m = len(nums1), len(nums2)
    result = []
    while i < n and j < m:
        if nums1[i] == nums2[j]:
            result.append(nums1[i])
            i += 1
        elif j > i:
            j += 1
            # continue
        # result.append(nums1[i])

    return result


# print(intersection([1, 2, 2, 1], [2, 2]))
# print(intersection([2], [2, 2]))
# print(intersection([2, 1], [1, 2]))
# print(intersection([4, 9, 5], [9, 4, 9, 8, 4]))


# 350. Intersection of Two Arrays II
def intersect(nums1, nums2):
    nums1.sort()
    nums2.sort()
    i = j = 0
    n, m = len(nums1), len(nums2)
    result = []
    while i < n and j < m:
        if nums1[i] == nums2[j]:
            result.append(nums1[i])
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        elif nums1[i] > nums2[j]:
            j += 1

    return result


# print(intersect([4, 9, 5], [9, 4, 9, 8, 4]))
# print(intersect([1, 2, 2, 1], [2, 2]))

