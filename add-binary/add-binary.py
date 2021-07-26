class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        remainder = 0
        newStr = ""
        
        while i >= 0 or j >= 0 or remainder == 1:
            total = 0
            
            if i >= 0:
                total += int(a[i])
            if j >= 0:
                total += int(b[j])
            if remainder == 1:
                total += remainder
            
            newStr += str(total % 2)
            remainder = total//2
            i -= 1
            j -= 1
                
        return newStr[::-1]
