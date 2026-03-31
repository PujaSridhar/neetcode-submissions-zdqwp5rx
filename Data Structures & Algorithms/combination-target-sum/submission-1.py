class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        def backtrack(remaining,path,start):
            if remaining < 0:
                return
            if remaining == 0:
                result.append(list(path))
            for i in range(start,len(nums)):
                path.append(nums[i])
                backtrack(remaining-nums[i],path,i)
                path.pop()
        backtrack(target,[],0)
        return result