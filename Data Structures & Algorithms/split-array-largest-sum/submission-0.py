class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left, right = max(nums), sum(nums)

        def canSplit(maxSum):
            pieces = 1
            curr = 0
            for num in nums:
                if curr + num <= maxSum:
                    curr += num
                else:
                    pieces += 1
                    curr = num
            return pieces <= k

        while left < right:
            mid = (left + right) // 2
            if canSplit(mid):
                right = mid
            else:
                left = mid + 1

        return left    