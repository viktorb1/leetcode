class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for t in tokens:
            if t in {'+', '-', '/', '*'}:
                y = stack.pop()
                x = stack.pop()
                if   t == '+': stack.append(x+y)
                elif t == '-': stack.append(x-y)
                elif t == '/': stack.append(int(x/y))
                elif t == '*': stack.append(x*y)
            else:
                stack.append(int(t))
        
        return stack.pop()