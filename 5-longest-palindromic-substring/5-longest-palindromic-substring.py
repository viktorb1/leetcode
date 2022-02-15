class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.m = ""
    
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1

            if r-l-1 > len(self.m):
                self.m = s[l+1:r]
                            
        for i,c in enumerate(s):
            expand(i, i)
            expand(i, i+1)
            
        return self.m
            
            
            
