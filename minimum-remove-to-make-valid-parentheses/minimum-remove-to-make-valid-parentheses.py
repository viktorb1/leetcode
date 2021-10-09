class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        sol = list(s)
        
        for idx, val in enumerate(s):
            if val == '(':
                stack.append(idx)
            elif val == ')':
                if stack:
                    stack.pop()
                else: # too many ')'
                    sol[idx] = ""
        
        while stack: # too many '('
            sol[stack.pop()] = ""
        
        return ''.join(sol)