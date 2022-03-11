class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = []

        for i in range(len(matrix)-1):
            if matrix[i][0] <= target < matrix[i+1][0]:
                row = matrix[i]
                break
        else:
            row = matrix[-1]
        
        i = bisect_left(row, target)
        return row[i] == target if i < len(row) else 0