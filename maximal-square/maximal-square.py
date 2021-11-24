class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        sol = 0
        
        for y, row in enumerate(matrix):
            for x, item in enumerate(row):
                if item == '1':                  
                    sol = max(self.getlargest(matrix, x, y), sol)
    
        return sol*sol

                
    def getlargest(self, m, x, y):
        
        sol = 2
        
        while x+sol-1 < len(m[0]) and y+sol-1 < len(m):

            for yy in range(y, y+sol):
                if m[yy][x+sol-1] == '0':
                    return sol-1

            for xx in range(x, x+sol):
                if m[y+sol-1][xx] == '0':
                    return sol-1
        
            sol += 1
            
        return sol-1
    