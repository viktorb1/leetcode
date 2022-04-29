class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        @cache
        def dfs(i, j, filterr):
            seen.add((i, j))
            for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if (x, y) not in seen and 0 <= x < len(heights) and 0 <= y < len(heights[0]):
                    if abs(heights[x][y] - heights[i][j]) <= filterr:
                        dfs(x, y, filterr)
            
        
        se_low, se_high = -1, max(max(heights, key=max))
        while se_low + 1 < se_high:
            seen = set()
            se_mid = (se_low + se_high) // 2
            dfs(0, 0, se_mid)
            if (len(heights)-1, len(heights[0])-1) in seen:
                se_high =  se_mid
            else:
                se_low = se_mid
            
        return se_high
            
            