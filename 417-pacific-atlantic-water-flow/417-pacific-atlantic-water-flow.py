class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        sol = []
        memo = {}
        
        def reachOcean(i, j, coord):
            if i == coord[0] or j == coord[1]:
                return True
            if (i, j, coord) in memo:
                return memo[(i, j, coord)]

            tmp = heights[i][j]
            heights[i][j] = float('inf')
            
            for x, y in ((i+1, j), (i, j+1), (i-1, j), (i, j-1)):
                if isInRange(x, y) and tmp >= heights[x][y] and reachOcean(x, y, coord):
                    heights[i][j] = tmp
                    return True
            
            heights[i][j] = tmp
            return False
        
        def isInRange(i, j):
            return i >= 0 and i < len(heights) and j >= 0 and j < len(heights[0])
        
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                memo[i, j, (0, 0)] = reachOcean(i, j, (0, 0))
                memo[i, j, (len(heights)-1, len(heights[0])-1)] = reachOcean(i, j, (len(heights)-1, len(heights[0])-1))
                
                if memo[i, j, (0, 0)] and memo[i, j, (len(heights)-1, len(heights[0])-1)]:
                    sol.append((i, j))
        
        return sol