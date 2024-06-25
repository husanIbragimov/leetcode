from typing import List, Iterable


def merge_to_arrays(arr1: List[int], arr2: List[int]) -> List[int]:
    i = j = 0
    result = []
    n, m = len(arr1), len(arr2)

    while i < n and j < m:
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    while i < n:
        result.append(arr1[i])
        i += 1

    while j < m:
        result.append(arr2[j])
        j += 1

    return result


def merge_to_arrays2(arr1: List[int], arr2: List[int]) -> Iterable[int]:
    i = j = 0
    n, m = len(arr1), len(arr2)

    while i < n and j < m:
        if arr1[i] < arr2[j]:
            yield arr1[i]
            i += 1
        else:
            yield arr2[j]
            j += 1

    while i < n:
        yield arr1[i]
        i += 1

    while j < m:
        yield arr2[j]
        j += 1


lst1 = [2, 5, 7, 8]
lst2 = [1, 3, 4, 6, 9, 10, 11]

print(merge_to_arrays(lst1, lst2))
print(merge_to_arrays2(lst1, lst2))
