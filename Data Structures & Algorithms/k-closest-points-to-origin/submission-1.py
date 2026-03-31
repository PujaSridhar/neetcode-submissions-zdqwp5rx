class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for (x,y) in points:
            distance = -(x*x+y*y)
            if len(max_heap) < k:
                heapq.heappush(max_heap,(distance,x,y))
            else:
                heapq.heappushpop(max_heap,(distance,x,y))
        return [[x,y] for (distance,x,y) in max_heap]