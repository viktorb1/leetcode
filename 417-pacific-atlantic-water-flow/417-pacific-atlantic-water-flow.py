class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        sol = []
        def reachOcean(i, j, oceans):
            if i == 0 or j == 0:
                oceans[0] = True
            if i == len(heights)-1 or j == len(heights[0])-1:
                oceans[1] = True
            if oceans[0] and oceans[1]:
                return True

            tmp = heights[i][j]
            heights[i][j] = float('inf')
            
            for x, y in ((i+1, j), (i, j+1), (i-1, j), (i, j-1)):
                if isInRange(x, y) and tmp >= heights[x][y] and reachOcean(x, y, oceans):
                    heights[i][j] = tmp
                    return True
            
            heights[i][j] = tmp
            return False
        
        def isInRange(i, j):
            return i >= 0 and i < len(heights) and j >= 0 and j < len(heights[0])
        
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if reachOcean(i,j, [False, False]):
                    sol.append((i, j))
                    
        return sol
                    
                    