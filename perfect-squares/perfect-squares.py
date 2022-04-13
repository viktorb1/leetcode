class Solution:
    def numSquares(self, n: int) -> int:
        amount = float('inf')
        
        @cache
        def updateMin(num, count): 
            nonlocal amount
            if count >= amount:
                return
            if num == 0:
                amount = min(amount, count)
                return

            for i in range(int(sqrt(num)), 0, -1):
                updateMin(num - i ** 2, count + 1)
        
        updateMin(n, 0)
        return amount
                