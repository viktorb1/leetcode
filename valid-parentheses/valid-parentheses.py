class Solution:
    def isValid(self, s: str) -> bool:
        track = []
        pairs = {'{':'}', '(':')', '[':']'}
        
        for i in s:
            if i in pairs.keys():
                track.append(i)
            else:
                if len(track) == 0 or i != pairs[track.pop()]:
                    return False 
        
        if len(track) != 0:
            return False
        
        return True
