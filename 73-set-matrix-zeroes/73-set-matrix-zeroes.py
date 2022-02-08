class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zeroCol = False
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    if j > 0:
                        matrix[0][j] = 0
                    else:
                        zeroCol = True
        
        for i in range(1, len(matrix[0])):
            if matrix[0][i] == 0:
                for j in range(len(matrix)):
                    matrix[j][i] = 0
            
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                for j in range(len(matrix[0])):
                    matrix[i][j] = 0
                    
        if zeroCol:
            for i in range(len(matrix)):
                matrix[i][0] = 0
