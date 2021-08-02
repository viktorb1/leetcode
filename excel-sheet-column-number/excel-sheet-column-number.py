class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        total = 0
        
        for i in range(len(columnTitle)):
            total += (ord(columnTitle[-(i+1)]) - ord('A') + 1) * pow(26, i)
            
        return total