class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific, atlantic = set(), set()
        rows = len(heights)
        cols = len(heights[0])
        
        
        def climb(i, j, set_container):
            set_container.add((i,j))
            for (x, y) in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if (0 <= x < rows) and (0 <= y < cols) and heights[i][j] <= heights[x][y] and (x, y) not in set_container:
                    climb(x, y, set_container)
            

        for r in range(rows):
            climb(r, 0, pacific)
            climb(r, cols-1, atlantic)
        
        for c in range(cols):
            climb(0, c, pacific)
            climb(rows-1, c, atlantic)
        
        return pacific.intersection(atlantic)