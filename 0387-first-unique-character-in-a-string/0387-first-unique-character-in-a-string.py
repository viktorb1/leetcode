class Solution:
    def firstUniqChar(self, s: str) -> int:
        chars = Counter(s)
        
        for i, c in enumerate(s):
            if chars[c] == 1:
                return i
        
        return -1