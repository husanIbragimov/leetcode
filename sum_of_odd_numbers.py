def sum_of_odd_numbers(n: int) -> int:
    if n % 2 == 0:
        return int((2 + 2 * (n // 2 - 1)) / 2 * (n // 2))
    return int((2 + 2 * (n // 2)) / 2 * (n // 2 + 1))


print(sum_of_odd_numbers(100))
print(sum_of_odd_numbers(5))
print(sum_of_odd_numbers(8))
print(sum_of_odd_numbers(16))


# O(1) vaqt
