class Solution:
    def addDigits(self, num: int) -> int:
        
        while num > 9:
            x = 0
            
            while num > 0:
                x += num % 10
                num //= 10
            
            num = x
            
        return num