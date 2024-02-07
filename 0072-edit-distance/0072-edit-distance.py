class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        def recur(w1, w2):
            if not w1: return len(w2)
            if not w2: return len(w1)
            if w1[0] == w2[0]: return recur(w1[1:], w2[1:])
            if (w1, w2) in memo:
                return memo[(w1,w2)]
            
            insert = 1 + recur(w1, w2[1:])
            delete = 1 + recur(w1[1:], w2)
            replace = 1 + recur(w1[1:], w2[1:])
            memo[(w1, w2)] = min(insert, delete, replace)
            return memo[(w1, w2)]
    
        return recur(word1, word2)