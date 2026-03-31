class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        m = len(matrix)
        n = len(matrix[0])
        left = 0
        right = m * n - 1
        while left <= right:
            mid = left + (right - left) // 2
            midVal = matrix[mid//n][mid%n]
            if midVal == target:
                return True
            elif midVal < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
