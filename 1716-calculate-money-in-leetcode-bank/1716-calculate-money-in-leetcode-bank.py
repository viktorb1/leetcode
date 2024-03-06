class Solution:
    def totalMoney(self, n: int) -> int:
        total = 0
        weeks = n//7 + 1
        m = 7
        
        for w in range(weeks-1):
            total += w*m + (m*(m+1))//2
        
        m = n % 7
        total += (weeks-1)*m + (m*(m+1))//2
        return total