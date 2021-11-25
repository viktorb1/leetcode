class Solution:
    def binaryGap(self, n: int) -> int:
        x = list(f'{n:b}')
        
        while x[-1] == '0':
            x.pop()
                   
        c = 0
        m = 0
        
        for i in x:
            if i == '0':
                c += 1
            else:
                if c > m:
                    m = c
                    
                c = 0
        
        if m > 0:
            return m+1
        elif len(x) > 1:
            return 1
        else:
            return 0