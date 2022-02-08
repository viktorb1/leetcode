class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        l = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    l.append((i, j))
                
        for i, j in l:
            for k in range(len(matrix[0])):
                matrix[i][k] = 0

            for k in range(len(matrix)):
                matrix[k][j] = 0
