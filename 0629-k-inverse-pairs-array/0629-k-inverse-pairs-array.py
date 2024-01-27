class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        dp = [[0] * (k+1) for _ in range(n+1)]
        
        for row in dp: # base case when k = 0
            row[0] = 1
        
        for i in range(1, n+1):
            for j in range(1, k+1):
                dp[i][j] = dp[i][j-1] + dp[i-1][j] - (dp[i-1][j-i] if j >= i else 0)
                # for m in range(min(i-1, j) + 1):
                #     dp[i][j] += dp[i-1][j-m]
        
        # dp[i][j] = dp[i-1][j-0] + dp[i-1][j-1] + dp[i-1][j-2] + ... + dp[i-1][j-(i-2)] + dp[i-1][j-(i-1)]
        # dp[i][j-1] = dp[i-1][j-1] + dp[i-1][j-2] + dp[i-1][j-3] + ... + dp[i-1][j-(i-1)] + dp[i-1][j-i]
        # notice the common terms cancel out when subtracting the two
        # dp[i][j] - dp[i][j-1] = dp[i-1][j-0] - dp[i-1][j-i]
        # dp[i][j] = dp[i][j-1] + dp[i-1][j-0] - dp[i-1][j-i]
        
        
        return dp[-1][-1] % (10**9+7)