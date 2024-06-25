class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        low = 0
        high = len(s) - 1
        while low < high:
            ...



hello_world = "Hello World"
s = "   fly me   to   the moon  "

solution = Solution()
print(solution.lengthOfLastWord(hello_world))
print(solution.lengthOfLastWord(s))
