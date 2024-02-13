class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def recur(s, p):
            if not s and not p:
                return True
            elif s and not p:
                return False
            elif not s and p:
                if len(p) > 1 and p[1] == "*":
                    return recur(s, p[2:])
                else:
                    return False
            
            if p[0] == ".":
                if len(p) > 1 and p[1] == "*":
                    if recur(s, p[2:]):
                        return True
                
                    for i, c in enumerate(s):
                        if recur(s[i+1:], p[2:]):
                            return True
                else:
                    return recur(s[1:], p[1:])
            elif len(p) > 1 and p[1] == "*":
                if p[0] != s[0]:
                    return recur(s, p[2:])
                
                if recur(s, p[2:]):
                    return True
                
                for i, c in enumerate(s):
                    if c != s[0]:
                        break
                    
                    if recur(s[i+1:], p[2:]):
                        return True
            elif s[0] == p[0]:
                return recur(s[1:], p[1:])
        
        return recur(s, p)