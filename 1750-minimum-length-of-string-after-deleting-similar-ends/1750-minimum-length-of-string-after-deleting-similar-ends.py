class Solution:
    def minimumLength(self, s: str, i=0) -> int:
        l, r = 0, len(s)-1
        if s[l] != s[r]: return len(s)
        
        while l < r and s[r] == s[l]:
            while s[l] == s[r] and l < r:
                l += 1
            
            while s[r] == s[l-1] and l <= r:
                r -= 1

        
        return r - l + 1