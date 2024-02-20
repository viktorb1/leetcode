class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = [-1] * n
        ans = []
        
        def dfs(cols, path):
            nonlocal ans, n
            r = len(path)
            if r == n:
                ans.append(path)
                return
            
            for c in range(n):
                cols[r] = c
                
                if is_valid(cols, r):
                    row = "." * n
                    dfs(cols, path + [row[:c] + "Q" + row[c+1:]])
        
        def is_valid(cols, r):
            for i in range(r):
                if abs(cols[i] - cols[r]) == r - i or cols[i] == cols[r]:
                    return False
            
            return True
        
        dfs([-1]*n, [])
        return ans

