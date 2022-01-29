class Solution:
    def fib(self, n: int) -> int:
        fibs = [0, 1]
        
        for i in range(n-1):
            fibs.append(fibs[-2] + fibs[-1])
        
        return fibs[n]