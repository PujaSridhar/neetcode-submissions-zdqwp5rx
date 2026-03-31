class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Step 1: Create a graph
        graph = defaultdict(list)
        for src, dst in tickets:
            heapq.heappush(graph[src], dst)
        
        # Step 2: DFS traversal
        result = []
        
        def dfs(node):
            while graph[node]:
                next_dest = heapq.heappop(graph[node])
                dfs(next_dest)
            result.append(node)
        
        dfs("JFK")
        
        # Step 3: Reverse the result list to get the right order
        return result[::-1]

       