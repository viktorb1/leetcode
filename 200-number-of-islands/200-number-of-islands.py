class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def flood(i,j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
                return
            
            grid[i][j] = '0'
            flood(i-1, j)
            flood(i+1, j)
            flood(i, j-1)
            flood(i, j+1)
            return 1
            
        count = 0
        for i,j in itertools.product(range(len(grid)), range(len(grid[0]))):
            if grid[i][j] == '1':
                count += flood(i, j)
                
        return count