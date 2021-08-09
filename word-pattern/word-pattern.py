class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(' ')
        mustMatch = {}
        seen = set()
        
        if len(s) != len(pattern):
            return False
        
        for i in range(len(s)):
            if pattern[i] not in mustMatch:
                if s[i] in seen:
                    return False
                
                mustMatch[pattern[i]] = s[i]
                seen.add(s[i])
            elif mustMatch[pattern[i]] != s[i]:
                return False
        
        return True
        
