from collections import defaultdict
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1

        # Buckets: index = frequency, value = list of numbers
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in freq.items():
            buckets[count].append(num)

        res = []
        for f in range(len(buckets) - 1, 0, -1):
            for num in buckets[f]:
                res.append(num)
                if len(res) == k:
                    return res