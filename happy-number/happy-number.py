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
            
            split = list(str(n))
            n = 0
            
            for i in split:
                n += pow(int(i), 2)
        
        