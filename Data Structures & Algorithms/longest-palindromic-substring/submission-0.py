class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""
        
        start, end = 0, 0
        
        for i in range(len(s)):
            len1 = self.expandAroundCenter(s, i, i)    # Odd length palindromes
            len2 = self.expandAroundCenter(s, i, i + 1) # Even length palindromes
            max_len = max(len1, len2)
            
            if max_len > (end - start):
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
        
        return s[start:end + 1]
    
    def expandAroundCenter(self, s: str, left: int, right: int) -> int:
        L, R = left, right
        while L >= 0 and R < len(s) and s[L] == s[R]:
            L -= 1
            R += 1
        return R - L - 1  # Length of the palindrome
       