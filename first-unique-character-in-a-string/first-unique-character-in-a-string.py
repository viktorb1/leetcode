class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        count = Counter(s)
        
        for i in count.keys():
            if count[i] == 1:
                return s.index(i)
            
        return -1
