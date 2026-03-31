class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        map = {}
        for num in nums:
            if num not in map:
                map[num] = 1
        count = 0
        for i in nums:
            if i - 1 not in map:
                a = i
                while a in map:
                    a += 1
                    count = max(count,a-i)
        return count