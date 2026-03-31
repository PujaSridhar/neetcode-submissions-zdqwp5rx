class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        seen = {}
        start = 0

        for i, char in enumerate(s):
            if char in seen and seen[char] >= start:
                start = seen[char] + 1
            seen[char] = i
            maxLength = max(maxLength, i - start + 1)
        return maxLength