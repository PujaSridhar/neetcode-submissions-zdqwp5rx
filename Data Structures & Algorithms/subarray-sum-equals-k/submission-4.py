class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefixSum = 0
        freq = {0:1}
        for num in nums:
            prefixSum += num
            if prefixSum - k in freq:
                count += freq[prefixSum - k]
            freq[prefixSum] = freq.get(prefixSum,0) + 1
        return count