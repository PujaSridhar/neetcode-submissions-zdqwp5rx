class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        
        if abs(target) > total or (target + total) % 2 != 0:
            return 0
        
        S = (target + total) // 2
        dp = [0] * (S + 1)
        dp[0] = 1
        
        for num in nums:
            for x in range(S, num - 1, -1):
                dp[x] += dp[x - num]
        
        return dp[S]
       