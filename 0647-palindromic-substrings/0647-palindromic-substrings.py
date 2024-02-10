class Solution:
    def countSubstrings(self, s: str) -> int:
        self.count = 0
        def expand(i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                self.count += 1
                i -=1
                j += 1
        
        for i in range(len(s)):
            expand(i, i)
            expand(i, i+1)
        
        return self.count