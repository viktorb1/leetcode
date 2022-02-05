class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        
        def dfs(i, j, visited, prev):
            if i < 0 or i >= rows or j < 0 or j >= cols or heights[i][j] < prev or (i, j) in visited:
                return
            
            visited.add((i, j))
            
            for x, y in ((i+1, j), (i, j+1), (i-1, j), (i, j-1)):
                dfs(x, y, visited, heights[i][j])
        
        for c in range(cols):
            dfs(0, c, pacific, 0)
            dfs(rows-1, c, atlantic, 0)
            
        for r in range(rows):
            dfs(r, 0, pacific, 0)
            dfs(r, cols-1, atlantic, 0)
            
        return pacific.intersection(atlantic)