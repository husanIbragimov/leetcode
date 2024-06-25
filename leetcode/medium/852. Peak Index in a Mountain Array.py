from typing import List
import time


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
start_time = time.time()
print(peakIndexInMountainArray(arr))
print("--- %s seconds ---" % (time.time() - start_time))

arr = [0, 2, 3, 1, 0]
start_time = time.time()
print(peakIndexInMountainArray(arr))
print("--- %s seconds ---" % (time.time() - start_time))

# answer: 1
# har bir to'g'ri qadam uchun +1
