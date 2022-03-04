class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cr = Counter(ransomNote)
        cm = Counter(magazine)
        
        for i in cr:
            if i not in cm or cr[i] > cm[i]:
                return False
        
        return True