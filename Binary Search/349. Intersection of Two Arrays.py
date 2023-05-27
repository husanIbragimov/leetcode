from typing import List


def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    set1 = set(nums1)
    set2 = set(nums2)
    result = []

    for i in set1:
        if i in set2:
            result.append(i)
    return result


print(intersection([1, 2, 2, 1], [2, 2]))
print(intersection([2], [2, 2]))
print(intersection([2, 1], [1, 2]))
print(intersection([4, 9, 5], [9, 4, 9, 8, 4]))
