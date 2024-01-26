class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:        
        
        @cache
        def dfs(i, j, rem):
            count = 0
            
            if i < 0 or i >= m or j < 0 or j >= n:
                return 1
            
            if rem:
                count += dfs(i+1, j, rem-1)
                count += dfs(i, j+1, rem-1)
                count += dfs(i-1, j, rem-1)
                count += dfs(i, j-1, rem-1)
            
            return count
        
        return dfs(startRow, startColumn, maxMove) % (pow(10, 9) + 7)