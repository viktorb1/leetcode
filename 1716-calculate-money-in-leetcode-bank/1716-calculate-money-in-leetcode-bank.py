class Solution:
    def totalMoney(self, n: int) -> int:
        total = 0
        weeks = n//7 + 1
        m = 7
        
        for w in range(weeks):
            if w == weeks-1: m = n % 7
            
            total += w*m + (m*(m+1))//2
        
        return total