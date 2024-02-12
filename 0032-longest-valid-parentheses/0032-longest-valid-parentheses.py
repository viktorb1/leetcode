class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        stack = []
        maxdist = 0
        
        for i, c in enumerate(s):
            if c == ')' and stack and stack[-1][1] == '(':
                stack.pop()
                j = stack[-1][0]+1 if stack else 0
                maxdist = max(maxdist, i-j+1)
            else:
                stack.append((i, c))
        
        return maxdist