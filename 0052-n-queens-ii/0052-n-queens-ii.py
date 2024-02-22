class Solution:
    def totalNQueens(self, n: int) -> int:
        count = 0
        cols = [-1] * n
        
        def dfs(cols, r):
            nonlocal count
            if r == n:
                count += 1
                return
            
            for c in range(n):
                cols[r] = c
                if self.is_valid(cols, r, c):
                    dfs(cols, r+1)
        
        dfs(cols, 0)
        return count
    
    def is_valid(self, cols, r1, c1):
        for r2, c2 in enumerate(cols[:r1]):
            if abs(r2-r1) == abs(c2-c1) or c1 == c2:
                return False
        return True