class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 0:
            return 0
        if n == 1:
            return cost[0]

        # Initialize dp array to store minimum cost to reach each step
        dp = [0] * n
        dp[0] = cost[0]
        dp[1] = cost[1]

        # Fill the dp array using the relation
        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])

        # The minimum cost to reach the top is the minimum of the last two steps
        return min(dp[n-1], dp[n-2])        