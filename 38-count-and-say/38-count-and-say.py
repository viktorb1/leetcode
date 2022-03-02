class Solution:
    def countAndSay(self, n: int) -> str:
        s = '1'
        
        for i in range(2, n+1):
            prev = ''
            count = 0
            new_s = ''
            for c in s:
                if c != prev:
                    if prev:
                        new_s += str(count) + prev
                    count = 1
                    prev = c
                else:
                    count += 1
            
            new_s += str(count) + prev
            s = new_s
        
        return s
                
            