class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        # Convert all stones to negative to simulate a max-heap
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)
        
        while len(max_heap) > 1:
            # Extract the two heaviest stones
            first = -heapq.heappop(max_heap)
            second = -heapq.heappop(max_heap)
            
            if first != second:
                # If they are not equal, push the difference back into the heap
                heapq.heappush(max_heap, -(first - second))
        
        # If there's one stone left, return its weight, otherwise return 0
        return -max_heap[0] if max_heap else 0       