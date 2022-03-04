class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        stack.append(0)
        
        for c in s:
            if c == '(':
                stack.append(0)
            else:
                v = stack.pop()
                w = stack.pop()
                stack.append(w + max(2 * v, 1));
            
        return stack[-1]