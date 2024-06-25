from typing import List


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
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


print(intersect([4, 9, 5], [9, 4, 9, 8, 4]))
print(intersect([1, 2, 2, 1], [2, 2]))
