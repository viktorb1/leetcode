class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(0, len(matrix)):
            j = 0
            first_ele = matrix[i][j]
            
            while i < len(matrix) and j < len(matrix[0]):
                if matrix[i][j] != first_ele:
                    return False
                i += 1
                j += 1
        
        
        for j in range(0, len(matrix[0])):
            i = 0
            first_ele = matrix[i][j]
            
            while i < len(matrix) and j < len(matrix[0]):
                if matrix[i][j] != first_ele:
                    return False
                i += 1
                j += 1
                
        return True