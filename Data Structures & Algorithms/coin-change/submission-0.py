class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize DP array with "infinity" for all indices greater than 0
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  # Base case: 0 coins needed to make the amount 0
        
        # Fill the DP array
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        
        # If dp[amount] is still infinity, it means we cannot make that amount
        return dp[amount] if dp[amount] != float('inf') else -1        