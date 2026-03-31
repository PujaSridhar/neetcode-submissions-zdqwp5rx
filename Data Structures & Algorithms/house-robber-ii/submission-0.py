class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        
        def rob_linear(nums: List[int]) -> int:
            prev1, prev2 = 0, 0
            for num in nums:
                current = max(prev2 + num, prev1)
                prev2 = prev1
                prev1 = current
            return prev1
        
        # Case 1: Rob houses from 0 to n-2
        case1 = rob_linear(nums[:-1])
        # Case 2: Rob houses from 1 to n-1
        case2 = rob_linear(nums[1:])
        
        return max(case1, case2)        