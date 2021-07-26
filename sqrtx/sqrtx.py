class Solution:
    def mySqrt(self, x: int) -> int:
        i = 1
        
        while i <= x:
            if i ** 2 > x:
                break
            else:
                i += 1
                
        
        return i - 1