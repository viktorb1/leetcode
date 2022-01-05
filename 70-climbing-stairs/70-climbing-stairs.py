class Solution:
    def climbStairs(self, n: int) -> int:
        a = 1
        b = 1
        sol = 1
        
        for _ in range(1, n):
            sol = a + b
            a, b = b, sol
            
        return sol
