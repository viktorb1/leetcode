class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        i, j = 0, 0
        output = []
        going_up = True
        
        for i in range(len(mat)):
            j = 0
            row = []
            
            while i >= 0 and j < len(mat[0]):
                row.append(mat[i][j])
                i -= 1
                j += 1
            
            if not going_up:
                output += row[::-1]
                going_up = True
            else:
                output += row
                going_up = False
            
        for j in range(1, len(mat[0])):
            i = len(mat) - 1
            row = []
            
            while i >= 0 and j < len(mat[0]):
                row.append(mat[i][j])
                i -= 1
                j += 1
            
            if not going_up:
                output += row[::-1]
                going_up = True
            else:
                output += row
                going_up = False

        return output