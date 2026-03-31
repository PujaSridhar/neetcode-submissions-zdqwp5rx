class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}
        for num in nums:
            if num in freq_dict:
                freq_dict[num] += 1
            else:
                freq_dict[num] = 1
        
        # Step 2: Use a heap to keep the top k frequent elements
        heap = []
        for num, freq in freq_dict.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        # Step 3: Extract the elements from the heap
        return [num for freq, num in heap]