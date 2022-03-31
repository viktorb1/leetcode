class Solution:
    def checkRecord(self, s: str) -> bool:
        absenses = 0
        
        for c in s:
            if c == 'A':
                absenses += 1
            if absenses == 2:
                return False
        
        for i in range(len(s)-3+1):
            if s[i:i+3] == 'LLL':
                return False
        
        return True