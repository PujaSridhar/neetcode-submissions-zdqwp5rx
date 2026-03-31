class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        
        # To keep track of points included in the MST
        in_mst = [False] * n
        
        # Min-heap to store (cost, point_index)
        min_heap = [(0, 0)]  # Start with the first point (index 0) with cost 0
        total_cost = 0
        edges_used = 0
        
        while edges_used < n:
            cost, u = heapq.heappop(min_heap)
            
            # If this point is already in MST, skip it
            if in_mst[u]:
                continue
            
            # Add the cost to the total cost
            total_cost += cost
            edges_used += 1
            in_mst[u] = True
            
            # Explore all edges from this point
            for v in range(n):
                if not in_mst[v]:
                    # Manhattan distance as the edge weight
                    dist = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                    heapq.heappush(min_heap, (dist, v))
        
        return total_cost        