class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0

        def dfs(i,currXOR):
            nonlocal total
            if i == len(nums):
                total += currXOR
                return 
            dfs(i+1,currXOR)
            dfs(i+1,currXOR ^ nums[i])
        dfs(0,0)
        return total