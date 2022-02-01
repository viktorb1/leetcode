class Solution:
        
    def tribonacci(self, n: int) -> int:
        memo = {}
        
        def helper(n):
            if n == 0:
                return 0
            elif n == 1:
                return 1
            elif n == 2:
                return 1
            elif n in memo:
                return memo[n]

            memo[n] = helper(n-1) + helper(n-2) + helper(n-3)
            return memo[n]
        
        return helper(n)