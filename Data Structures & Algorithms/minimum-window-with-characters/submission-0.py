class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
    
    # Count the characters in t
        t_count = Counter(t)
        current_count = Counter()
    
        required = len(t_count)
        formed = 0
    
        left = 0
        min_length = float('inf')
        min_window_start = 0
    
        for right, char in enumerate(s):
            current_count[char] += 1
        
            if char in t_count and current_count[char] == t_count[char]:
                formed += 1
        
            while left <= right and formed == required:
                char = s[left]
            
                if (right - left + 1) < min_length:
                    min_length = right - left + 1
                    min_window_start = left
            
                current_count[char] -= 1
                if char in t_count and current_count[char] < t_count[char]:
                    formed -= 1
            
                left += 1
    
        if min_length == float('inf'):
            return ""
    
        return s[min_window_start:min_window_start + min_length]