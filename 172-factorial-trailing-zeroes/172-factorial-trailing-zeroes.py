class Solution:
    def trailingZeroes(self, n: int) -> int:
        numfives = 0
        
        for i in range(5, n+1):
            while i % 5 == 0:
                numfives += 1
                i = i // 5
        
        return numfives