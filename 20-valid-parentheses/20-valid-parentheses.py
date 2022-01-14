class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_par = {'(':')', '[':']', '{':'}'}
        
        for i in s:
            if i in open_par.keys():
                stack.append(i)
            elif not stack or i != open_par[stack.pop()]:
                return False
        
        return False if stack else True