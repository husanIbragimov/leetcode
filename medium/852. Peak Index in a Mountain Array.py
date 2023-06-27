from typing import List


def peakIndexInMountainArray(arr: List[int]) -> int:
    low = 0
    high = len(arr) - 1
    while low < high:
        mid = (low + high) // 2
        if arr[mid] < arr[mid + 1]:
            low = mid + 1
        else:
            high = mid
    return low


arr = [0, 1, 0]
print(peakIndexInMountainArray(arr))
arr = [0, 2, 1, 0]
print(peakIndexInMountainArray(arr))
