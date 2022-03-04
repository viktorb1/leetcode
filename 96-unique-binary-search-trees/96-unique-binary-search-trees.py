class Solution:
    @cache
    def numTrees(self, n: int) -> int:
        if n <= 1:
            return 1
        
        count = 0
        for i in range(1, n+1):
            count += self.numTrees(i-1) * self.numTrees(n-i)
        return count