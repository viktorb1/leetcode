class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n+1)
        
        for rem in range(1, n+1):
            max_val = 0
            for i in range(1, rem+1):
                max_val = max(max_val, i * dp[rem-i], i*(rem-i))
            dp[rem] = max_val
        
        return dp[-1]