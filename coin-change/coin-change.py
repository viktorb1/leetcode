class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        return self.coinChangeHelper(coins, amount, memo)

    def coinChangeHelper(self, coins: List[int], amount: int, memo: Dict[int, int]) -> int:
        if amount == 0:
            return 0
        
        minCoins = float('inf') 
        
        if amount in memo:
            return memo[amount]
        else:
            for coin in coins:
                if coin <= amount:
                    cal = self.coinChangeHelper(coins, amount - coin, memo)

                    if cal != -1:
                        minCoins = min(minCoins, cal + 1)
        
        
        memo[amount] = minCoins
        return -1 if minCoins == float('inf') else minCoins
