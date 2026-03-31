class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        map={}
        for i in nums:
            if i not in map:
                map[i]=1
        count=0
        for j in nums:
            if j-1 not in map:
                a=j
                while a in map:
                    a+=1
                    count = max(count,a-j)
        return count
        