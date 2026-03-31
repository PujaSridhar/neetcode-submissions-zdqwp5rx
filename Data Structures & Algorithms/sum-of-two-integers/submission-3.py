class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32-bit integer mask
        MASK = 0xFFFFFFFF
        
        # Loop until there's no carry
        while b != 0:
            # Calculate carry
            carry = (a & b) & MASK
            
            # Sum without carry
            a = (a ^ b) & MASK
            
            # Shift carry by 1 and mask to keep within 32 bits
            b = (carry << 1) & MASK
        
        # If a is a positive number within the 32-bit range, return it
        if a <= 0x7FFFFFFF:
            return a
        else:
            # If a is negative, convert to a proper Python negative integer
            return ~(a ^ MASK)      