class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def isSafe(board, row, col):
            # Check this column on upper side
            for i in range(row):
                if board[i][col] == 'Q':
                    return False
            
            # Check upper diagonal on left side
            for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
                if board[i][j] == 'Q':
                    return False
            
            # Check upper diagonal on right side
            for i, j in zip(range(row, -1, -1), range(col, n)):
                if board[i][j] == 'Q':
                    return False
            
            return True
        
        def solve(row):
            if row == n:
                result.append([''.join(row) for row in board])
                return
            
            for col in range(n):
                if isSafe(board, row, col):
                    board[row][col] = 'Q'
                    solve(row + 1)
                    board[row][col] = '.'
        
        result = []
        board = [['.'] * n for _ in range(n)]
        solve(0)
        return result        