class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        curr = 0

        for i in range(len(s)):            
            for j in range(curr, len(t)):
                if t[j] == s[i]:
                    curr = j+1
                    break
            else:
                return False
        
        return True