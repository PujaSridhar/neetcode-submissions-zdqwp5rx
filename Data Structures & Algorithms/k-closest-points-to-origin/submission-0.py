class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Create a max-heap to store the k closest points
        max_heap = []
        
        for (x, y) in points:
            dist = -(x * x + y * y)  # Use negative distance to simulate max-heap
            if len(max_heap) < k:
                heapq.heappush(max_heap, (dist, x, y))
            else:
                heapq.heappushpop(max_heap, (dist, x, y))
        
        # Extract the k closest points from the heap
        return [[x, y] for (dist, x, y) in max_heap]