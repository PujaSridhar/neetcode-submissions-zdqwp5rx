class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_freq = 0
        max_length = 0
        char_count = {}
        for right in range(len(s)):
            char = s[right]
            char_count[char] = char_count.get(char,0) + 1
            max_freq = max(max_freq,char_count[char])
            while (right - left+1) - max_freq > k:
                left_char = s[left]
                char_count[left_char] -= 1
                left += 1
            max_length = max(max_length,right-left+1)
        return max_length   