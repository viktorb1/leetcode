class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_start, row_end = 0, len(matrix) - 1
        col_start, col_end = 0, len(matrix[0]) - 1
        
        while row_start < row_end:
            for i in range(0, col_end-col_start):
                save = matrix[row_start][col_start+i]
                matrix[row_start][col_start+i] = matrix[row_end-i][col_start]
                matrix[row_end-i][col_start] = matrix[row_end][col_end-i]
                matrix[row_end][col_end-i] = matrix[row_start+i][col_end]
                matrix[row_start+i][col_end] = save

            row_start += 1
            row_end -= 1
            col_start += 1
            col_end -= 1
        