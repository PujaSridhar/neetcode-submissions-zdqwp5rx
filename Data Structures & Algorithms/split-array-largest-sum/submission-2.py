class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def split(maxSum):
            pieces = 1
            currentSum = 0
            for i in nums:
                if currentSum + i <= maxSum:
                    currentSum += i
                else:
                    pieces += 1
                    currentSum = i
            return pieces <= k
        
        left, right = max(nums), sum(nums)
        while left < right:
            mid = (right + left) // 2
            if split(mid):
                right =  mid
            else:
                left = mid + 1
        return left