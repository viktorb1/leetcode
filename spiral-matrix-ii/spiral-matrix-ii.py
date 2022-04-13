class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        arr = [[0] * n for i in range(n)]
        row_start, col_start = 0, 0
        row_end, col_end = n-1, n-1
        num = 1
        
        while row_start <= row_end and col_start <= col_end:
            for i in range(col_start, col_end + 1):
                arr[row_start][i] = num
                num += 1
            row_start += 1
            
            for i in range(row_start, row_end + 1):
                arr[i][col_end] = num
                num += 1
            col_end -= 1
            
            for i in range(col_end, col_start-1, -1):
                arr[row_end][i] = num
                num += 1
            row_end -= 1
            
            for i in range(row_end, row_start-1, -1):
                arr[i][col_start] = num
                num += 1
            col_start += 1
        
        return arr