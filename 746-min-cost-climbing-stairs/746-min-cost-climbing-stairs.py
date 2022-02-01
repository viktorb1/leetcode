class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost))
        dp[0] = 0
        dp[1] = min(cost[0], cost[1])
        
        for i, n in enumerate(cost[2:], 2):
            dp[i] = min(cost[i] + dp[i-1], cost[i-1] + dp[i-2])
        
        return dp[-1]