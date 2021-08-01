class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        for i in s:
            if not i.isalnum():
                s = s.replace(i, "")
        
        s = s.lower()
        
        for i in range(len(s) // 2):
            if s[i] != s[len(s) - i - 1]:
                return False
        
        return True