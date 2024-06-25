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

print(is_perfect_square(value))
# math.sqrt(16) --> True
