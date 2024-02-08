class Solution:
    def numSquares(self, n: int) -> int:   
        dp = [0] + [float('inf')] * n
                    
        for i in range(n+1):
            for j in range(int(sqrt(n)), 0, -1):
                if i >= j*j:
                    dp[i] = min(dp[i], 1 + dp[i-j*j])

        return dp[-1]