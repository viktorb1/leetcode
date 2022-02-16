class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        @cache
        def dfs(i, j):
            if i >= len(grid) or j >= len(grid[0]):
                return float('inf')
            elif (i, j) == (len(grid) - 1, len(grid[0]) - 1):
                return grid[i][j]
            
            return grid[i][j] + min(dfs(i+1, j), dfs(i, j+1))
        
        return dfs(0, 0)