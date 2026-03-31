class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for price in range(len(prices)-1):
            if prices[price] < prices[price+1]:
                profit += prices[price+1] - prices[price]
        return profit