class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        memo = {}
        def dfs(w1, w2):
            if not w1 or not w2:
                return 0
            elif (w1, w2) in memo:
                return memo[(w1, w2)]
            
            if w1[0] == w2[0]:
                memo[(w1, w2)] = 1 + dfs(w1[1:], w2[1:])
            else:
                memo[(w1, w2)] = max(dfs(w1[1:], w2), dfs(w1, w2[1:]))
            
            return memo[(w1, w2)]
        
        len_lcs = dfs(word1, word2)
        return (len(word1) - len_lcs) + (len(word2) - len_lcs)