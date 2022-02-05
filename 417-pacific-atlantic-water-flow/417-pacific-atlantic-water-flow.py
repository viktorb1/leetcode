class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        sol = []
        
        def reachPacific(i, j):
            if i == 0 or j == 0:
                return True

            tmp = heights[i][j]
            heights[i][j] = float('inf')
            
            
            for x, y in ((i+1, j), (i, j+1), (i-1, j), (i, j-1)):
                if isInRange(x, y) and tmp >= heights[x][y] and reachPacific(x, y):
                    heights[i][j] = tmp
                    return True
            
            heights[i][j] = tmp
            return False
        
        
        def reachAtlantic(i, j):
            if i == len(heights) - 1 or j == len(heights[0]) - 1:
                return True

            tmp = heights[i][j]
            heights[i][j] = float('inf')
            
            for x, y in ((i+1, j), (i, j+1), (i-1, j), (i, j-1)):
                if isInRange(x, y) and tmp >= heights[x][y] and reachAtlantic(x, y):
                    heights[i][j] = tmp
                    return True
            
            heights[i][j] = tmp
            return False
        
        
        def isInRange(i, j):
            return i >= 0 and i < len(heights) and j >= 0 and j < len(heights[0])
        
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if reachAtlantic(i, j) and reachPacific(i, j):
                    sol.append((i, j))
                    
        return sol
                    
                    