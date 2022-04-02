class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        p_op = '+'
        stack = []
        
        for i, c in enumerate(s):
            if c.isdigit():
                num = num*10 + int(c)
            
            if c in "*/+-" or i == len(s) - 1:
                if p_op == '+': stack.append(num)
                elif p_op == '-': stack.append(-num)
                elif p_op == '*': stack.append(stack.pop()*num)
                elif p_op == '/': stack.append(int(stack.pop()/num))
                num = 0
                p_op = c

        return sum(stack)
            