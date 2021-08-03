class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        for i in range(len(s)):
            for j in range(len(s)):
                if s[j] == s[i] and j != i:
                    break
                elif j == len(s) - 1:
                    return i
            
        return -1