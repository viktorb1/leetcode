class Solution:
    def longestPalindrome(self, s: str) -> str:
        m = [""]
    
        def expand(l, r, m):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1

            l += 1
            r -= 1

            if r-l+1 > len(m[0]):
                m[0] = s[l:r+1]
                
                            
        for i,c in enumerate(s):
            expand(i, i, m)
            
        for i,c in enumerate(s[:-1]):
            expand(i, i+1, m)
            
        return m[0]
            
            
            
