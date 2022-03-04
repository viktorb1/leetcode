class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        for i in range(1, len(s)+1):
            if s[i:] + s[:i] == goal:
                return True
        
        return False