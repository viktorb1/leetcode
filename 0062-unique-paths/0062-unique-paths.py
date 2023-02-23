class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        
        def dfs(m, n):
            if (m, n) in memo:
                return memo[(m, n)]
            elif m == 1 and n == 1:
                return 1

            total = 0

            if m > 0:
                total += dfs(m-1, n)
            if n > 0:
                total += dfs(m, n-1)
            
            memo[(m, n)] = total
            return total
        
        return dfs(m,n)