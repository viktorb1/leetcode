class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        vals = [1] * n
        total = n
        i = len(vals) - 1
        
        while total < k:
            if vals[i] == 26:
                i -= 1
            vals[i] += 1
            total += 1
        
        return ''.join([chr(ord('a') + v - 1) for v in vals])
            