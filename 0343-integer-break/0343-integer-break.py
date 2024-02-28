class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n+1)
        
        for i in range(1, n+1):
            max_val = 0
            for j in range(1, i+1):
                max_val = max(max_val, j * dp[i-j], j*(i-j))
            dp[i] = max_val
        
        return dp[-1]