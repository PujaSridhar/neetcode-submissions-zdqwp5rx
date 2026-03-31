class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        num_islands = 0

        def dfs(r, c):
            # if the current cell is out of bounds or water ('0'), stop the DFS
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
                return
            # mark the current cell as visited by setting it to '0'
            grid[r][c] = '0'
            # visit all adjacent cells (up, down, left, right)
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':  # found an unvisited land
                    num_islands += 1   # increment the island count
                    dfs(r, c)          # start DFS to mark all connected lands

        return num_islands
        