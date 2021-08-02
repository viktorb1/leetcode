class Solution:
    def trailingZeroes(self, n: int) -> int:
        numtwos = 0
        numfives = 0
        numtens = 0
        
        for i in range(2, n+1):
            while i % 10 == 0:
                numtens += 1
                i //= 10
            while i % 5 == 0:
                numfives += 1
                i //= 5
            if i % 2 == 0:
                numtwos += i // 2

        return min(numtwos, numfives) + numtens
