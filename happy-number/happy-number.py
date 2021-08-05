class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while 1:           
            if n == 1:
                return True
            elif n in seen:
                return False
            else:
                seen.add(n)

            j = n
            n = 0
            
            while j > 0:
                n += pow(j % 10, 2)
                j //= 10
