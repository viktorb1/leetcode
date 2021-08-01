class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        min = prices[0]
        
        for i in range(0, len(prices)):
                if prices[i] < min:
                    min = prices[i]
                elif prices[i] - min > max:
                    max = prices[i] - min;
                    
        return max