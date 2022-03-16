class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:        
        @cache
        def dfs(i, row):
            if row >= len(triangle):
                return 0

            return triangle[row][i] + min(dfs(i, row+1), dfs(i+1, row+1))
            
        return dfs(0, 0)
            