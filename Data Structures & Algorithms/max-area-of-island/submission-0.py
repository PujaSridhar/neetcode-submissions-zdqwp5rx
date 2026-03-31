class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        max_area = 0

        def dfs(r, c):
            # if the current cell is out of bounds or water ('0'), stop the DFS
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
                return 0
            # mark the current cell as visited by setting it to '0'
            grid[r][c] = 0
            # count the current cell
            area = 1
            # visit all adjacent cells (up, down, left, right) and add their areas
            area += dfs(r + 1, c)
            area += dfs(r - 1, c)
            area += dfs(r, c + 1)
            area += dfs(r, c - 1)
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:  # found an unvisited land
                    # calculate the area of this island and update max_area
                    max_area = max(max_area, dfs(r, c))

        return max_area
      