class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        i = 1
            
        while i < n:
            i *= 2;
            
        return True if i == n else False
        
        
        
        