class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Build the graph
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        # Dijkstra's algorithm
        min_heap = [(0, k)]  # (time, node)
        dist = {i: sys.maxsize for i in range(1, n + 1)}
        dist[k] = 0
        
        while min_heap:
            current_time, u = heapq.heappop(min_heap)
            
            if current_time > dist[u]:
                continue
            
            for v, w in graph[u]:
                time = current_time + w
                if time < dist[v]:
                    dist[v] = time
                    heapq.heappush(min_heap, (time, v))
        
        max_dist = max(dist.values())
        return max_dist if max_dist < sys.maxsize else -1
        