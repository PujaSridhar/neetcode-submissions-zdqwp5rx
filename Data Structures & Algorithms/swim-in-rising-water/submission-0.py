class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # Priority queue to store (max elevation so far, row, col)
        pq = [(grid[0][0], 0, 0)]
        # Visited matrix to keep track of the cells that have been processed
        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True
        
        # Directions for moving up, down, left, right
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while pq:
            # Pop the cell with the minimum max elevation encountered so far
            time, x, y = heapq.heappop(pq)
            
            # If we've reached the bottom-right corner, return the time
            if x == n-1 and y == n-1:
                return time
            
            # Explore the neighbors
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    # Push the maximum elevation encountered so far to the priority queue
                    heapq.heappush(pq, (max(time, grid[nx][ny]), nx, ny))
        
        return -1  # This line should never be reached
        