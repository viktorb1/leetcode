class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        amounts = [float(inf)] * (amount+1)
        amounts[0] = 0
        
        for idx, amount in enumerate(amounts):
            for coin in coins:
                if coin <= idx:
                    amounts[idx] = min(amounts[idx], 1 + amounts[idx - coin])
        
        if amounts[-1] == float('inf'):
            return -1
        else:
            return amounts[-1]