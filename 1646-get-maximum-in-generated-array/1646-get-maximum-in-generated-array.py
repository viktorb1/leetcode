class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = 0
        
        if n > 0:
            dp[1] = 1
            
        max_num = 0
        
        for i in range(0, n+1):
            if i & 1 == 0:
                dp[i] = dp[i//2]
            else:
                dp[i] = dp[i//2] + dp[i//2+1]
            
            max_num = max(max_num, dp[i])
            
        return max_num