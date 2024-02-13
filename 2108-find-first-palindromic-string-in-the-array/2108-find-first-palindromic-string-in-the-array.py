class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for s in words:
            m = len(s)//2
            if s[:m] == s[m+1:][::-1] or s[:m] == s[m:][::-1]:
                return s
        
        return ""