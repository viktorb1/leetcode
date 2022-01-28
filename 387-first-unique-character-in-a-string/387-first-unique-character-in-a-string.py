class Solution:
    def firstUniqChar(self, s: str) -> int:
        chars = Counter(s)
        uniques = set()
        
        for c in chars:
            if chars[c] == 1:
                uniques.add(c)
        
        for i, c in enumerate(s):
            if c in uniques:
                return i
            
        return -1