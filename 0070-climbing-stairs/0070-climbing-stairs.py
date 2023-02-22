class Solution:
    def __init__(self):
        self.memo = {}
    
    def climbStairs(self, n: int) -> int:
        memo = [1, 1] + [0] * (n-1)
        
        for i in range(2, len(memo)):
            memo[i] = memo[i-1] + memo[i-2]

        return memo[-1]
