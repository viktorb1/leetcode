class Solution:
    def integerBreak(self, n: int) -> int:
        @cache
        def dfs(rem):
            if not rem:
                return 0;
            
            max_val = 0
            for i in range(1, rem+1):
                max_val = max(max_val, i * dfs(rem-i), i*(rem-i))
            return max_val
        
        return dfs(n)