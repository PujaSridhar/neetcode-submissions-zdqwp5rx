class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Bellman-Ford approach
        dp = [[float('inf')] * (k + 2) for _ in range(n)]
        dp[src][0] = 0
        
        for i in range(1, k + 2):
            dp[src][i] = 0  # Initialize source cost to 0 for all stops
            for u, v, cost in flights:
                dp[v][i] = min(dp[v][i], dp[u][i-1] + cost)
        
        min_cost = min(dp[dst][:k + 2])
        
        return min_cost if min_cost != float('inf') else -1        