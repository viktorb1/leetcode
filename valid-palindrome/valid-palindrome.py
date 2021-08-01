class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        st = ""
        
        for i in s:
            if i.isalnum():
                st += i.lower()
        
        for i in range(len(st) // 2):
            if st[i] != st[len(st) - i - 1]:
                return False
        
        return True
