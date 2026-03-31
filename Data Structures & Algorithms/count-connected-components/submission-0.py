class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Create the adjacency list representation of the graph
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Keep track of visited nodes
        visited = [False] * n
        
        def dfs(node):
            stack = [node]
            while stack:
                current = stack.pop()
                for neighbor in graph[current]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        stack.append(neighbor)
        
        # Count the number of connected components
        count = 0
        for i in range(n):
            if not visited[i]:
                # If the node is not visited, it's a new component
                count += 1
                visited[i] = True
                dfs(i)
        
        return count        