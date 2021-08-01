class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        prices = [99999] +  prices
        i = 1
        
        while i < len(prices) - 1:
            
            while i < len(prices) - 1 and (not prices[i-1] > prices[i] or not prices[i+1] > prices[i]):
                i += 1
            
            while i < len(prices) - 1 and prices[i+1] > prices[i]:
                profit += prices[i+1] - prices[i]
                i += 1
                
        return profit
