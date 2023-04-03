"""
Linear Search
"""


def linear_search(arr, item):
    i = 0
    for n in range(len(arr)):
        i = i + 1
        if arr[n] == item:
            return f'n: {n}; i: {i};'
    return None


my_arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
my_item = 10


# print(linear_search(my_arr, my_item))


# def two_sum(nums, target):
#     """
#     :type nums: List[int]
#     :type target: int
#     :rtype: List[int]
#     """
#     nums = []
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 a = []
#             return a[i, j]
#
#
# sum = [5, 6, 2, 4]
# tar = 8
# print(two_sum(sum, tar))

def is_power_of_two(num) -> bool:
    bit_count = 0
    while num != 0:
        print(num)
        bit_count += num & 1
        print("bit_count", bit_count)
        num = num >> 1
        print("num", num)

    return bit_count == 1


# print(is_power_of_two(15))
# print(7 & 1)


def sum_of_odd_numbers(n: int) -> int:
    a = 1
    an = n
    k = n - 1 // 2 + 1
    print(k)
    s = (a + an) // 2 * n

    return s


# print(sum_of_odd_numbers(8))


# hashmap
def is_anagram(word1: str, word2: str) -> bool:
    counter1 = dict()
    counter2 = dict()

    for char in word1:
        if char not in counter1:
            counter1[char] = 1
            continue

        counter1[char] += 1

    for char in word2:
        if char not in counter2:
            counter2[char] = 1
            continue

        counter2[char] += 1

    return counter1 == counter2


# print(is_anagram('alam', 'lama'))

def build_counter(word):
    counter = dict()
    for char in word:
        if char not in counter:
            counter[char] = 1
            continue

        counter[char] += 1
    return counter



def is_anagram1(word1: str, word2: str) -> bool:
    counter1 = build_counter(word1)
    counter2 = build_counter(word2)


    return counter1 == counter2


print(is_anagram('alam', 'lama'))
print(is_anagram('mosh', 'oshm'))
print(is_anagram('olma', 'molo'))

def build_counter2(word):
    counter = dict()
    for char in word:
        if char not in counter:
            counter[char] = 1
            continue

        counter[char] += 1
    return counter



def is_anagram2(word1: str, word2: str) -> bool:
    counter1 = build_counter2(word1)

    for char in word2:
        counter1[char] -= 1

    for val in counter1.values():
        if val != 0:
            return False
    # return True
    #  alohida 
    for char in word2:
        counter1[char] -= 1
    return all(val == 0 for val in counter1.values())



print(is_anagram('alam', 'lama'), 'dicrement')
