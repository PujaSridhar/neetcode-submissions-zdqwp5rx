 
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for i in nums:
            if i in dict:
                return True
            dict[i] = 1  # Initialize the count to 1 when the key is first added
        return False
