class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        @cache
        def dfs(x,y):
            if y < 0 or y >= len(matrix[0]):
                return float('inf')
            
            if x == len(matrix):
                return 0
            
            left = dfs(x+1, y-1)
            middle = dfs(x+1, y)
            right = dfs(x+1, y+1)
            
            return matrix[x][y] + min(left, middle, right)
        
        min_val = float('inf')
        for i in range(len(matrix[0])):
            min_val = min(min_val, dfs(0, i))
        
        return min_val