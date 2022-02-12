class Solution:
    def trailingZeroes(self, n: int) -> int:
        numfives = 0
        numtens = 0
        
        for i in range(5, n+1):
            if i % 10 == 0:
                numtens += 1
                i //= 10
            while i % 5 == 0:
                numfives += 1
                i //= 5

        return numfives + numtens