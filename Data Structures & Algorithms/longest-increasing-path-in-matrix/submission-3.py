from functools import lru_cache
import sys
sys.setrecursionlimit(1000001)
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        rows, cols = len(matrix), len(matrix[0])
        memo = {}
        @lru_cache(None)
        def dfs(r,c):
            res = 1
            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr,nc = r+dr, c+dc
                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                    res = max(res, 1+dfs(nr,nc))
            memo[(r,c)] = res
            return res
        maxPath = 0
        for r in range(rows):
            for c in range(cols):
                maxPath = max(maxPath,dfs(r,c))
        return maxPath


