class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        min_arr = [0] * n
        max_arr = [0] * n
        min_arr[0] = prices[0]
        max_arr[n - 1] = prices[n - 1]
        for i in range(1, n):
            min_arr[i] = min(min_arr[i - 1], prices[i])
            max_arr[n - 1 - i] = max(max_arr[n - i], prices[n - 1 - i])
        
        profit = 0
        for i in range(n):
            profit = max((max_arr[i] - min_arr[i]), profit)
        
        return profit