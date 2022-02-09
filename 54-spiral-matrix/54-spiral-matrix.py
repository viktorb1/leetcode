class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        sol = []
        row_start, row_end = 0, len(matrix) - 1
        col_start, col_end = 0, len(matrix[0]) - 1
        
        while row_start <= row_end and col_start <= col_end:
            for i in range(col_start, col_end + 1):
                sol.append(matrix[row_start][i])
            row_start += 1
            
            for i in range(row_start, row_end + 1):
                sol.append(matrix[i][col_end])
            col_end -= 1
            
            if row_start > row_end or col_start > col_end:
                break
            
            for i in range(col_end, col_start - 1, -1):
                sol.append(matrix[row_end][i])
            row_end -= 1
        
            for i in range(row_end, row_start - 1, -1):
                sol.append(matrix[i][col_start])
            col_start += 1
            
        return sol
