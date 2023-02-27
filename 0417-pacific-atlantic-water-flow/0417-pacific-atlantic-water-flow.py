class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        atlantic_visited, pacific_visited = set(), set()
        
        def climb(i, j, p_or_a):
            p_or_a.add((i,j))
            for (x,y) in [(i-1,j),(i+1, j),(i,j-1),(i,j+1)]:
                if 0 <= x < rows and 0 <= y < cols and (x,y) not in p_or_a and heights[x][y] >= heights[i][j]:
                    climb(x,y,p_or_a)
        
        for r in range(rows):
            climb(r, 0, pacific_visited)
            climb(r, cols-1, atlantic_visited)
        
        for c in range(cols):
            climb(0, c, pacific_visited)
            climb(rows-1, c, atlantic_visited)
        
        return atlantic_visited.intersection(pacific_visited)