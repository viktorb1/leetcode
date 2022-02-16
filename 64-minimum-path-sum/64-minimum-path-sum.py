class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        @cache
        def dfs(i, j):
            if i >= r or j >= c:
                return float('inf')
            elif (i, j) == (r - 1, c - 1):
                return grid[i][j]
            
            return grid[i][j] + min(dfs(i+1, j), dfs(i, j+1))
        
        return dfs(0, 0)