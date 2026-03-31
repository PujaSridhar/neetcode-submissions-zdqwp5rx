class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # A tree with n nodes must have exactly n - 1 edges
        if len(edges) != n - 1:
            return False
        
        # Create an adjacency list representation of the graph
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Use BFS to check connectivity and detect cycles
        visited = set()
        
        def bfs(node):
            queue = [node]
            while queue:
                curr = queue.pop(0)
                for neighbor in graph[curr]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
        
        # Start BFS from node 0
        visited.add(0)
        bfs(0)
        
        # Check if all nodes are visited
        return len(visited) == n        