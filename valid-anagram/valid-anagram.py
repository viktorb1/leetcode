class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}
        for i in s:
            if not i in seen:
                seen[i] = 1
            else:
                seen[i] += 1
        
        for i in t:
            if not i in seen:
                return False
            else:
                seen[i] -= 1
            
        for i in seen.values():
            if i != 0:
                return False
            
        return True