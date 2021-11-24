class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        sol = 0
        
        for x, row in enumerate(matrix):
            for y, item in enumerate(row):
                if item == '1':                  
                    sol = max(self.getlargest(matrix, x, y), sol)
    
        return sol*sol

                
    def getlargest(self, m, x, y):
        
        sol = 2
        
        while x+sol-1 < len(m) and y+sol-1 < len(m[0]):

            for yy in range(y, y+sol):
                if m[x+sol-1][yy] == '0':
                    return sol-1

            for xx in range(x, x+sol):
                if m[xx][y+sol-1] == '0':
                    return sol-1
        
            sol += 1
            
        return sol-1
