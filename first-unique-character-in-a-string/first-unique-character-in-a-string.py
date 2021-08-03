class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        seen = {}
        
        for i in range(len(s)):
            if not s[i] in seen:
                seen[s[i]] = Entry(i)
            else:
                seen[s[i]].num += 1
                
                
        for i in seen:
            if seen[i].num == 1:
                return seen[i].idx
            
        return -1
    

class Entry:
    def __init__(self, i: int): 
        self.num = 1
        self.idx = i
