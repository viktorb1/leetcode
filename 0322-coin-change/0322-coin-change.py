class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:        
        @cache
        def change(coins, amount):            
            if amount == 0:
                return 0
            elif amount < 0:
                return float('inf')
            
            coins_needed = float('inf')
            for i, coin in enumerate(coins):
                    coins_needed = min(coins_needed, 1 + change(coins, amount-coin))
            return coins_needed
                
        res = change(tuple(coins), amount)
        return res if res != float('inf') else -1