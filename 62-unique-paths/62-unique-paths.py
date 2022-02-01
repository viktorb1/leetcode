class Solution:
    def __init__(self):
        self.memo = {}
    
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 and n == 1:
            return 1
        elif m < 1 or n < 1:
            return 0
        elif (m, n) in self.memo:
            return self.memo[(m,n)]
        
        self.memo[(m, n)] = self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)
        return self.memo[(m, n)]