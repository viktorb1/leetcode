class Solution:
    def mySqrt(self, x: int) -> int:
        
        low = 1
        high = x
        i = 0
        
        while high - low >= 0:
            i = (low + high) // 2

            if i ** 2 > x:
                high = i - 1
            elif (i+1) ** 2 > x:
                break
            else:
                low = i + 1
                
        return i