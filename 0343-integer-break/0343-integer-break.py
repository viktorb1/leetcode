class Solution:
    def integerBreak(self, n: int) -> int:
        memo = {}
        def dfs(rem):
            if rem == 1:
                return 1;
            if rem in memo:
                return memo[rem]
            
            max_val = 0
            for i in range(1, rem+1):
                max_val = max(max_val, i * dfs(rem-i), i*(rem-i))
            memo[rem] = max_val
            return max_val
        
        return dfs(n)