class Solution:
    def reverse(self, x: int) -> int:
        
        negative = False
        rev = 0
        
        if x < 0:
            negative = True
            x *= -1;
        
        while x > 0:
            rev = rev * 10 + x % 10
            x //= 10
        
        if negative:
            rev *= -1;
        
        if rev < -pow(2,31) or rev > pow(2,31) - 1:
            return 0
        else:
            return rev
        
        
        