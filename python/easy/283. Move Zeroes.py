from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        count = 0
        for i, num in enumerate(nums):
            if num == 0:
                count += 1
                continue

            nums[i], nums[i - count] = nums[i - count], nums[i]

        return nums


nums = [0, 1, 0, 3, 12]
sol = Solution()
print(sol.moveZeroes(nums))
