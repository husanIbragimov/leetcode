import time

from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low = ans = 0
        high = len(nums) - 1
        
        while low < high:
            if nums[low] < nums[high]:
                low += 1
                ans = high
            else:
                ans = low
                high -= 1

        return ans


sol = Solution()
start_time = time.time()
print(sol.findPeakElement([1, 2, 3, 1]))
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
print(sol.findPeakElement([1, 2, 1, 3, 5, 6, 4]))
print("--- %s seconds ---" % (time.time() - start_time))
