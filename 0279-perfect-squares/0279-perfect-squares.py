class Solution:
    def numSquares(self, n: int) -> int:   
        memo = {}
        
        def dfs(n):
            if not n: return 0
            if n in memo: return memo[n]
            
            ans = float('inf')
            for j in range(int(sqrt(n)), 0, -1):
                if n >= j*j:
                    ans = min(ans, 1 + dfs(n-j*j))
                    
            memo[n] = ans
            return ans
        
        return dfs(n)