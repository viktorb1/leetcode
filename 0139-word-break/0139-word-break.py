class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        
        def dfs(i=0):
            if i == len(s):
                return True
            elif i in memo:
                return memo[i]
            
            can_break_remain = False
            for w in wordDict:
                if s[i:i+len(w)] == w:
                    can_break_remain |= dfs(i+len(w))
            
            memo[i] = can_break_remain
            return can_break_remain
    
        return dfs()