class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def maketr(state, prices, own):
            if not prices: return 0
            val1 = -prices[0] + maketr(1, prices[1:], True)
            val2 = maketr(0, prices[1:], own)
            val3 = prices[0] + maketr(2, prices[2:], False) if own else float('-inf')
            return max(val1, val2, val3)
        
        return maketr(0, tuple(prices), False)