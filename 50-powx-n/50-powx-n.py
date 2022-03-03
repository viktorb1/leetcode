class Solution:
    def myPow(self, x: float, n: int) -> float:
        @cache
        def rec(x, n):    
            if n == 0:
                return 1
            elif n < 0:
                return rec(1/x, -n)
            elif n % 2 == 1:
                newN = n - 1
                return x * rec(x, newN/2) * rec(x, newN/2)
            else:
                return rec(x, n/2) * rec(x, n/2)
        return rec(x, n)