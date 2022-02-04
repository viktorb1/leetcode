class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        d = 0
        
        for c in s:
            if c == '(':
                d += 1
            elif c == ')':
                d -= 1
            depth = max(depth, d)
        
        return depth