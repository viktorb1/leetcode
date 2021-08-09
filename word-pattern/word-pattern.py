class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(' ')
        mustMatch = {}
        seen = set()
        
        if len(s) != len(pattern):
            return False
        
        for i in range(len(pattern)):
            if pattern[i] not in mustMatch: # we ran into a new character
                if s[i] in seen: # if word isn't new for new character
                    return False
                else: # otherwise add it
                    mustMatch[pattern[i]] = s[i]
                    seen.add(s[i])
            elif mustMatch[pattern[i]] != s[i]:
                return False
        
        return True
