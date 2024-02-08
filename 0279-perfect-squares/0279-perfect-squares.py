class Solution:
    def numSquares(self, n: int) -> int:   
        dp = [0] + [float('inf')] * n
                    
        for k in range(n+1):
            for j in range(int(sqrt(n)), 0, -1):
                if k >= j*j:
                    dp[k] = min(dp[k], 1 + dp[k-j*j])

        return dp[-1]