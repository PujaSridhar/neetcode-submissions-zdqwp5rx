class Solution:
    def canPartitionKSubsets(self, nums, k):
        total = sum(nums)
        if total % k != 0:
            return False
        
        target = total // k
        n = len(nums)
        nums.sort(reverse=True)
        
        dp = [-1] * (1 << n)
        dp[0] = 0

        for mask in range(1 << n):
            if dp[mask] == -1:
                continue
            for i in range(n):
                if not (mask & (1 << i)):
                    if dp[mask] + nums[i] <= target:
                        newMask = mask | (1 << i)
                        dp[newMask] = (dp[mask] + nums[i]) % target
        
        return dp[(1 << n) - 1] == 0
       