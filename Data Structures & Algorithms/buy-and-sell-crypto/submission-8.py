class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = float("inf")
        for i in prices:
            if i < minPrice:
                minPrice = i
            elif i - minPrice > maxProfit:
                maxProfit = i - minPrice
        return maxProfit
