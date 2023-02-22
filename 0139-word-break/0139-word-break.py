class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        
        def dfs(i=0):
            if i == len(s):
                return True
            elif i in memo:
                return memo[i]
            
            starts = False
            for w in wordDict:
                if s[i:i+len(w)] == w:
                    starts |= dfs(i+len(w))
            
            memo[i] = starts
            return starts
    
        return dfs()