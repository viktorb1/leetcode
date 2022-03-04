class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        points = 1
        total = 0
        
        for i, c in enumerate(s):
            if c == '(':
                points *= 2
            elif s[i-1:i+1] == '()':
                total += points // 2
                points //= 2
            elif c == ')':
                points //= 2
        
        return total