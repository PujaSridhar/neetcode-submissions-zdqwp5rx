class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap,num)
            else:
                if heap[0] < num:
                    heapq.heappop(heap)
                    heapq.heappush(heap,num)
        return heapq.heappop(heap)    