class Solution:
    def divisorGame(self, n: int) -> bool:
        dp = [False] * (n+1)
        
        for m in range(1, n+1):
            for i in range(1, m):
                if m % i == 0 and dp[m - i] == False:
                    dp[m] = True
            
        return dp[n]