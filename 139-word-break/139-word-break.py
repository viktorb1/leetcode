class Solution:
    
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        def wordBreakHelper(s, i=0):
            if i == len(s):
                return True
            elif i in memo:
                return memo[i]

            for word in wordDict:
                if word == s[i:i+len(word)]:
                    memo[i] = wordBreakHelper(s, i+len(word))
                    if memo[i]:
                        return True

            return False
        
        memo = {}
        return wordBreakHelper(s)