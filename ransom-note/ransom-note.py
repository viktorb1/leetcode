class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        have = {}
        
        for i in magazine:
            if not i in have:
                have[i] = 1
            else:
                have[i] += 1
                
            
        for i in ransomNote:
            if not i in have or have[i] == 0:
                return False
            if have[i] > 0:
                have[i] -= 1
    
        return True