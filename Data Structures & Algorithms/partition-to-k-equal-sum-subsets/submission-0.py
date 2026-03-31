class Solution:
    def canPartitionKSubsets(self, nums, k):
        total = sum(nums)
        if total % k != 0:
            return False
        
        target = total // k
        nums.sort(reverse=True)
        
        # Quick fail: if largest element > target
        if nums[0] > target:
            return False
        
        buckets = [0] * k

        def backtrack(i):
            if i == len(nums):
                return True
            
            for j in range(k):
                if buckets[j] + nums[i] <= target:
                    buckets[j] += nums[i]
                    if backtrack(i + 1):
                        return True
                    buckets[j] -= nums[i]
                
                # 🔥 Pruning:
                # If this bucket was empty and didn't work,
                # no need to try other empty buckets
                if buckets[j] == 0:
                    break
            
            return False

        return backtrack(0)
       