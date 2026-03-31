class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        start = 0
        char_count = {}
        for i,char in enumerate(s):
            if char in char_count and char_count[char] >= start:
                start = char_count[char] + 1
            char_count[char] = i 
            max_length = max(max_length,i-start+1)
        return max_length