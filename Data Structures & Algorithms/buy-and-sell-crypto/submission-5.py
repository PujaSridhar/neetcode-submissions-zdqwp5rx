class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        v = 1e10
        profit = 0
        for i in prices:
            v = min(v, i)
            profit = max(profit, i - v)
        
        return profit
