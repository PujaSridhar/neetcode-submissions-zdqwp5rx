class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        def backtrack(start,path,target):
            if target == 0:
                result.append(list(path))
            elif target < 0:
                return
            for i in range(start,len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                backtrack(i+1,path+[candidates[i]],target-candidates[i])
        backtrack(0,[],target)
        return result