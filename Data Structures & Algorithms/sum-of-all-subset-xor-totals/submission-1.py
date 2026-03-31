class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0
        def dfs(i,curr_sum):
            nonlocal total
            if i == len(nums):
                total += curr_sum
                return
            dfs(i+1,curr_sum)
            dfs(i+1,curr_sum^nums[i])
        dfs(0,0)
        return total    