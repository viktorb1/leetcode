class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [1] + [0]*(len(s))
        
        for i in range(1, len(dp)):
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            if i > 1 and 0 < int(s[i-2:i]) <= 26 and s[i-2] != '0':
                dp[i] += dp[i-2]
            
        return dp[-1]