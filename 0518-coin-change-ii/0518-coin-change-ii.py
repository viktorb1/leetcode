class Solution:
    def change(self, amount: int, coins: List[int]) -> int:        
        @cache
        def dfs(total, i=0):            
            if total == 0:
                return 1
            
            if total < 0 or i == len(coins):
                return 0

            return dfs(total - coins[i], i) + dfs(total, i+1)
        
        return dfs(amount)