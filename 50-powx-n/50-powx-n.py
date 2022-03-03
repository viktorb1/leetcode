class Solution:
    def myPow(self, x: float, n: int) -> float:
        memo = {}
        def rec(x, n):
            if (x, n) in memo:
                return memo[(x, n)]
            elif n == 0:
                return 1
            
            val = 0
            if n < 0:
                val = rec(1/x, -n)
            elif n % 2 == 1:
                newN = n - 1
                val = x * rec(x, newN/2) * rec(x, newN/2)
            else:
                val = rec(x, n/2) * rec(x, n/2)
            memo[(x, n)] = val
            return val
            
        return rec(x, n)