class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        @cache
        def dfs(i, j):
            maxpath = 0
            for x,y in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]):
                    if matrix[x][y] > matrix[i][j]:
                        maxpath = max(1 + dfs(x, y), maxpath)
                
            return maxpath
        
        maxpath = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                maxpath = max(1 + dfs(i, j), maxpath)
                
        return maxpath