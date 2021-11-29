class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        elif s1 == s2:
            return True
        
        for i in range(len(s2)):
            for j in range(i+1, len(s2)):
                if s1[:i] + s1[j] + s1[i+1:j] + s1[i] + s1[j+1:] == s2:
                    return True
                
        return False
    