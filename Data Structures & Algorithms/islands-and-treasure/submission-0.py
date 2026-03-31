class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return
        
        m, n = len(grid), len(grid[0])
        INF = 2147483647
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Initialize the BFS queue
        queue = deque()
        
        # Add all treasure chest cells to the queue
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    queue.append((i, j))
        
        # Perform BFS
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                # Check if the new position is within bounds and is a land cell (INF)
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == INF:
                    # Update the distance to the nearest treasure chest
                    grid[nx][ny] = grid[x][y] + 1
                    # Add the new position to the queue
                    queue.append((nx, ny))
