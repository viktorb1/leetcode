class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def dfs(s, p):
            if not s and (not p or set(p) == {'*'}):
                return True
            elif not s or not p:
                return False
            
            if p[0] == "*":
                if dfs(s[1:], p) or dfs(s, p[1:]):
                    return True
            elif p[0] == '?' or s[0] == p[0]:
                if dfs(s[1:], p[1:]):
                    return True
            else:
                return False
        
        return dfs(s, p)