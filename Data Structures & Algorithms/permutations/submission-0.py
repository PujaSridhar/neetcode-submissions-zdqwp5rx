class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(start):
            # If we reach the end of the array, we found a permutation
            if start == len(nums):
                result.append(nums[:])  # Make a copy of nums and add to result
                return
            
            for i in range(start, len(nums)):
                # Swap the current element with the start element
                nums[start], nums[i] = nums[i], nums[start]
                # Recurse with the next element in the array
                backtrack(start + 1)
                # Backtrack (undo the swap)
                nums[start], nums[i] = nums[i], nums[start]

        backtrack(0)
        return result        