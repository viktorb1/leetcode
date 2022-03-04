class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        points = 1
        maxp = 1
        total = 0
        
        for i, c in enumerate(s):
            if c == '(':
                stack.append(points)
                points *= 2
            elif s[i-1:i+1] == '()':
                total += stack.pop()
                points //= 2
            elif c == ')':
                stack.pop()
                points //= 2
        
        return total