class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0
        
        def dfs(i, curr_xor):
            nonlocal total
            if i == len(nums):
                total += curr_xor
                return
            
            # Exclude nums[i]
            dfs(i + 1, curr_xor)
            
            # Include nums[i]
            dfs(i + 1, curr_xor ^ nums[i])
        
        dfs(0, 0)
        return total       