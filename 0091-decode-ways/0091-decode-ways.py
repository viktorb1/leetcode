class Solution:
    def numDecodings(self, s: str) -> int:
        @cache
        def decode(i):
            
            if i < 0:
                return 1
            
            total = 0

            if s[i] != '0':
                total += decode(i-1)
            if i >= 1 and 0 < int(s[i-1:i+1]) <= 26 and s[i-1] != '0':
                total += decode(i-2)
            
            return total
    
        return decode(len(s)-1)