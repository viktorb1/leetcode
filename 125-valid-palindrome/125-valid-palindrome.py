class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        
        while l < r:
            while l < len(s) and not (s[l].isalpha() or s[l].isnumeric()): l += 1
            while r > 0 and not (s[r].isalpha() or s[r].isnumeric()): r -= 1
                
            if l > r:
                break
            
            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1
        
        return True
            
            