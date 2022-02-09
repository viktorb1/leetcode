class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        start_row, end_row = 0, n - 1
        start_col, end_col = 0, n - 1
        sol = []
        val = 1
        
        while start_row <= end_row and start_col <= end_col:
            for i in range(start_col, end_col + 1):
                matrix[start_row][i] = val
                val += 1
            start_row += 1
            
            for i in range(start_row, end_row + 1):
                matrix[i][end_col] = val
                val += 1
            end_col -= 1
            
            if start_row > end_row or start_col > end_col:
                break
        
            for i in range(end_col, start_col - 1, -1):
                matrix[end_row][i] = val
                val += 1
            end_row -= 1
        
            for i in range(end_row, start_row - 1, -1):
                matrix[i][start_col] = val
                val += 1
            start_col += 1
        
        return matrix