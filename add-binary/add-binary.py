class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        remainder = 0
        newStr = ""
        
        while i >= 0 or j >= 0 or remainder == 1:
            total = 0
            
            while i >= 0 and j >= 0:
                total = int(a[i]) + int(b[j]) + remainder
            elif i >= 0:
                total = int(a[i]) + remainder
            elif j >= 0:
                total = int(b[j]) + remainder
            else:
                total = remainder
            
            newStr = str(total % 2) + newStr
            remainder = total//2
            i -= 1
            j -= 1
            
                
        return newStr
