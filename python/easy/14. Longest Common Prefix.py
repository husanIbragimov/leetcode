from typing import List


def longestCommonPrefix(strs: List[str]):
    word = ""
    strs = sorted(strs)
    low = strs[0]
    high = strs[-1]
    i = 0
    while len(low) <= len(high):
        if len(low) < 2:
            return low
        if low[i] != high[i]:
            return word
        word += low[i]
        i += 1
    return word


print(longestCommonPrefix(["flower", "flow", "flight"]))
print(longestCommonPrefix(["dog", "racecar", "car"]))
print(longestCommonPrefix(["g"]))
print(longestCommonPrefix(["flower", "flower", "flower", "flower"]))
