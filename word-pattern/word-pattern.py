class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(' ')
        mustMatch = {}
        alreadySeen = set()
        
        if len(s) != len(pattern):
            return False
        
        for i in range(len(s)):
            if pattern[i] not in mustMatch:
                if s[i] in alreadySeen:
                    return False
                
                mustMatch[pattern[i]] = s[i]
                alreadySeen.add(s[i])
                
        for i in range(len(s)):
            if mustMatch[pattern[i]] != s[i]:
                return False
        
        return True
        