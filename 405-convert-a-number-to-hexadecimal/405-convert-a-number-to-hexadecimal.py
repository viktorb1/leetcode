class Solution:
    def toHex(self, num: int) -> str:
        sol = []
        
        if num < 0:
            num = pow(2, 32) + num
        elif num == 0:
            return '0'
        
        while num > 0:
            sol.append('0123456789abcdef'[num % 16])
            num //= 16
            
            
        return ''.join(sol[::-1])
            