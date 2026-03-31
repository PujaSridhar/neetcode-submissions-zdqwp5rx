class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dict = {}
        for num in nums:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1
        n = len(nums)
        return [num for num, v in dict.items() if v > n//3]