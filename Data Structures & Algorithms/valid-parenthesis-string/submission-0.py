class Solution:
    def checkValidString(self, s: str) -> bool:
        low = 0  # Minimum number of unbalanced '(' that must be closed
        high = 0 # Maximum number of unbalanced '(' that could exist
        
        for char in s:
            if char == '(':
                low += 1
                high += 1
            elif char == ')':
                low -= 1
                high -= 1
            else:  # char == '*'
                low -= 1
                high += 1
            
            # We can't have more ')' than '(' at any point
            if high < 0:
                return False
            
            # We can't have negative low because '*' can act as empty
            low = max(low, 0)
        
        # If low is 0, then all '(' have been balanced
        return low == 0        