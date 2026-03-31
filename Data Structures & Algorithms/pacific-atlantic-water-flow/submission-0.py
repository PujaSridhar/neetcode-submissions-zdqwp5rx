class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        
        m, n = len(heights), len(heights[0])
        
        pacific_reachable = set()
        atlantic_reachable = set()
        
        def dfs(r, c, reachable, prev_height):
            if (
                r < 0 or r >= m or c < 0 or c >= n or
                (r, c) in reachable or
                heights[r][c] < prev_height
            ):
                return
            reachable.add((r, c))
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for dr, dc in directions:
                dfs(r + dr, c + dc, reachable, heights[r][c])
        
        # Perform DFS from all cells adjacent to the Pacific Ocean
        for i in range(m):
            dfs(i, 0, pacific_reachable, heights[i][0])  # Left border
            dfs(i, n - 1, atlantic_reachable, heights[i][n - 1])  # Right border
        
        for j in range(n):
            dfs(0, j, pacific_reachable, heights[0][j])  # Top border
            dfs(m - 1, j, atlantic_reachable, heights[m - 1][j])  # Bottom border
        
        # Find the intersection of cells reachable by both oceans
        result = list(pacific_reachable & atlantic_reachable)
        
        return result        