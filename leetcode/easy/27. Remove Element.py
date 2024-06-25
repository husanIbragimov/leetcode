from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for i, num in enumerate(nums):
            if num == val:
                count += 1
                continue

            nums[i], nums[i - count] = nums[i - count], nums[i]
        return len(nums) - count


nums = [3, 2, 2, 3]
nums_2 = [0, 1, 2, 2, 3, 0, 4, 2]
sol = Solution()
print(sol.removeElement(nums, 3))
print(sol.removeElement(nums_2, 2))
