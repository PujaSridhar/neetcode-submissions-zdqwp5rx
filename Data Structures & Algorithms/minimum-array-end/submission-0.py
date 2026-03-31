class Solution:
    def minEnd(self, n: int, x: int) -> int:
        k = n - 1
        bit = 0
        ans = x
        
        while k > 0:
            # if this bit is 0 in x, we can use it
            if (x & (1 << bit)) == 0:
                if (k & 1):
                    ans |= (1 << bit)
                k >>= 1
            bit += 1
        
        return ans        