class Solution:
    def longestPalindrome(self, s: str) -> str:
        m = ""
    
        def expand(l, r):
            nonlocal m
            
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1

            if r-l-1 > len(m):
                m = s[l+1:r]
                            
        for i,c in enumerate(s):
            expand(i, i)
            expand(i, i+1)
            
        return m
            
            
            
