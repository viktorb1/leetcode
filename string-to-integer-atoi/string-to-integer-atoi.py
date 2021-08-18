class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        negative = False
        num = 0
        
        # remove pluses and minuses before numbers
        if len(s) > 0 and s[0] == '-':
            s = s[1:]
            negative = True
        elif len(s) > 0 and s[0] == '+':
            s = s[1:]

            
        # remove characters after numbers
        i = 0
        while i < len(s) and s[i] >= '0' and s[i] <= '9':
                i += 1
        
        s = s[:i]
    
        # build number from string
        for i in s:
            num *= 10
            num += ord(i) - ord('0')
        

        # handle negative cases
        if negative:
            return max(-num, -2147483648)
        else:
            return min(num, 2147483647)