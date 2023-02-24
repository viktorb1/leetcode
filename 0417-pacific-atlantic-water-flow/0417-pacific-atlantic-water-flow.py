class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific, atlantic = set(), set()
        rows = len(heights)
        cols = len(heights[0])
        
        
        def climb(i, j, set_container):
            set_container.add((i,j))
            for (x, y) in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if not (0 <= x < rows) or not (0 <= y < cols) or heights[i][j] > heights[x][y] or (x, y) in set_container:
                    continue
                else:
                    climb(x, y, set_container)
            

        for r in range(rows):
            climb(r, 0, pacific)
            climb(r, cols-1, atlantic)
        
        for c in range(cols):
            climb(0, c, pacific)
            climb(rows-1, c, atlantic)
        
        return pacific.intersection(atlantic)