class Solution:
    def convertToBase7(self, num: int) -> str:
        neg = '-' if num < 0 else ''
        num = abs(num)
        ans = ''
        
        while num > 0:
            ans = str((num % 7)) + ans
            num //= 7
        
        return neg + ans if ans else '0'