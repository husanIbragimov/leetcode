# 5. Longest Palindromic Substring
# Given a string s, return the longest palindromic substring in s.

# Manacher algorithm
def longestPalindrome(s: str) -> str:
    def preprocess(s):
        n = len(s)
        if n == 0:
            return "^$"
        result = "^"
        for i in range(n):
            result += "#" + s[i]
        result += "#$"
        return result

    T = preprocess(s)
    N = len(T)
    P = [0] * N
    C, R = 0, 0

    for i in range(1, N - 1):
        mirror = 2 * C - i
        if R > i:
            P[i] = min(R - i, P[mirror])

        # Attempt to expand palindrome centered at i
        while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
            P[i] += 1

        # If palindrome centered at i expands past R, adjust center and radius
        if i + P[i] > R :
            C, R = i, i + P[i]

    # Find the maximum element in P
    max_len, max_center = max((n, i) for i, n in enumerate(P))
    start = (max_center - max_len) // 2
    end = start + max_len
    return s[start:end]



print(longestPalindrome("babad"))
print(longestPalindrome("kiyik"))
print(longestPalindrome("anora"))
print(longestPalindrome("cbbd"))
print(longestPalindrome("kuchimla"))
