class Solution:
    def maximum69Number (self, num: int) -> int:
        num = list(str(num))
        l = 0
        
        while l < len(num) and num[l] == '9':
            l += 1
        
        if l < len(num):
            num[l] = '9'
            
        return int(''.join(num))