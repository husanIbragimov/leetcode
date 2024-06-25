# 704. Binary Search

def search(nums, target) -> int:
    low = 0
    high = len(nums) - 1
    while low <= high:

        mid = (low + high) // 2
        guess = nums[mid]
        if guess < target:
            low = mid + 1
        else:
            high = mid - 1

        if guess == target:
            return mid

    return -1

# 1. print(search([9], -9)) -> result: -1
# 2. print(search([9], 9)) -> result: 0
# 3. print(search([-1, 0, 3, 5, 9, 12], 9)) -> result: 4
