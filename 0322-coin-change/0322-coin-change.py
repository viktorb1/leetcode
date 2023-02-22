from collections import defaultdict

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:        
        memo = {}
        
        def change(coins, amount, memo):
            if amount == 0:
                return 0
            elif amount < 0:
                return float('inf')
            elif amount in memo:
                return memo[amount]
            
            smallest_coins = float('inf')
            for c in coins:
                smallest_coins = min(smallest_coins, 1+change(coins, amount-c, memo))
            memo[amount] = smallest_coins
            return memo[amount]
    
        res = change(coins, amount, memo)
        return res if res != float('inf') else -1