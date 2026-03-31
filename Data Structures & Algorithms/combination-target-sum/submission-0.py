class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(remaining, path, start):
            if remaining < 0:
                return  # Exceeded the sum, stop the exploration
            if remaining == 0:
                result.append(list(path))
                return  # Found a combination that adds up to the target
            
            for i in range(start, len(nums)):
                # Include the number nums[i] and continue exploring
                path.append(nums[i])
                backtrack(remaining - nums[i], path, i)  # Not i + 1 because we can reuse the same element
                path.pop()  # Backtrack, remove the last number added
        
        backtrack(target, [], 0)
        return result
        