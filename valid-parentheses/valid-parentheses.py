class Solution:
    def isValid(self, s: str) -> bool:
        paren = [];
        
        for i in s:
            if i == '(' or i == '[' or i == '{':
                paren.append(i);
            else:
                if not paren:
                    return False
                
                curr = paren.pop();
                
                if (i == ')' and curr != '(' 
                    or i == ']' and curr != '[' 
                    or i == '}' and curr != '{'):
                    return False
        
        return True if not paren else False