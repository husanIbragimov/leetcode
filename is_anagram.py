from collections import defaultdict


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


print(is_anagram('shom', 'mosh'))


def build_counter(word: str):
    counter = dict()
    for char in word:
        if char not in counter:
            counter[char] = 1
            continue
        counter[char] += 1
    # print(counter)
    return counter


def is_anagram2(word1: str, word2: str) -> bool:
    counter1 = build_counter(word1)
    counter2 = build_counter(word2)

    return counter1 == counter2


print(is_anagram2('soom', 'mosh'))


def new_build_counter(word: str):
    counter = defaultdict(int)
    for char in word:
        counter[char] += 1
    # print(counter)
    return counter


def is_anagram3(word1: str, word2: str) -> bool:
    counter = new_build_counter(word1)

    for char in word2:
        counter[char] -= 1

    for val in counter.values():
        if val != 0:
            return False

    return True


print(is_anagram3('alam', 'olma'))


def is_anagram4(word1: str, word2: str) -> bool:
    counter = new_build_counter(word1)

    for char in word2:
        counter[char] -= 1

    return all(val == 0 for val in counter.values())

# faster

print(is_anagram4('alam', 'alma'))
