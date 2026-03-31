class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        efforts = [[float('inf')] * cols for _ in range(rows)]
        efforts[0][0] = 0

        minHeap = [(0, 0, 0)]  # (effort, row, col)
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while minHeap:
            effort, r, c = heapq.heappop(minHeap)

            if r == rows - 1 and c == cols - 1:
                return effort

            if effort > efforts[r][c]:
                continue

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    new_effort = max(effort, abs(heights[r][c] - heights[nr][nc]))
                    if new_effort < efforts[nr][nc]:
                        efforts[nr][nc] = new_effort
                        heapq.heappush(minHeap, (new_effort, nr, nc))

        return 0       