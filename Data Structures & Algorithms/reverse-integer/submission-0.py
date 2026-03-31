class Solution:
    def reverse(self, x: int) -> int:
        # Define the 32-bit integer range
        INT_MAX = 2**31 - 1  # 2147483647
        INT_MIN = -2**31     # -2147483648
        
        # Store the sign and work with the absolute value of x
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        # Reverse the digits
        reversed_x = 0
        while x != 0:
            # Pop the last digit of x and push it to reversed_x
            pop = x % 10
            x //= 10
            # Check for overflow before actually updating reversed_x
            if reversed_x > (INT_MAX - pop) // 10:
                return 0  # Return 0 in case of overflow
            reversed_x = reversed_x * 10 + pop
        
        # Reapply the original sign
        reversed_x *= sign
        
        # Final check to ensure it's within the 32-bit integer range
        if reversed_x < INT_MIN or reversed_x > INT_MAX:
            return 0
        
        return reversed_x        