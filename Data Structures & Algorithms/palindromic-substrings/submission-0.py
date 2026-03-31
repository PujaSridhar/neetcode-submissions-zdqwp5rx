class Solution:
    def countSubstrings(self, s: str) -> int:
        def expandAroundCenter(s, left, right):
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count
        
        total_palindromes = 0
        
        for i in range(len(s)):
            # Count odd length palindromes centered at i
            total_palindromes += expandAroundCenter(s, i, i)
            # Count even length palindromes centered at i and i+1
            total_palindromes += expandAroundCenter(s, i, i + 1)
        
        return total_palindromes
        