class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        letter = 0
        
        for c in t:
            letter += ord(c)
            
        for c in s:
            letter -= ord(c)
            
        return chr(letter)