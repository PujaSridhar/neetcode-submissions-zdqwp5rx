class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            currentSum = 0
            while n > 0:
                n, digits = divmod(n,10)
                currentSum += digits ** 2
            n = currentSum
            if n in seen:
                return False
            seen.add(n)
        return True