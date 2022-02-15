class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {'(':')', '[':']', '{':'}'}
        
        for c in s:
            if c in brackets.keys():
                stack.append(c)
            elif c in brackets.values():
                if not stack:
                    return False
                elif brackets[stack.pop()] != c:
                    return False
        
        return len(stack) == 0
                    