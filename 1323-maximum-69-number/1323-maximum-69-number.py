class Solution:
    def maximum69Number (self, num: int) -> int:
        idx = -1
        n = num
        i = 0
        
        while n > 0:
            if n % 10 == 6:
               idx = i 
            i += 1
            n = n // 10
        
        return num + 3*10**idx if idx != -1 else num