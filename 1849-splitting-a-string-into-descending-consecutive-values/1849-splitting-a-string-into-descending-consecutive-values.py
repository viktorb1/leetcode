class Solution:
    def splitString(self, s: str) -> bool:
        
        @lru_cache
        def helper(prev, s):
            if not s:
                return True
            
            for i in range(1, len(s)+1):
                x = int(s[:i])

                if prev - x == 1:
                    if helper(x, s[i:]):
                        return True
            
            return False
        
        for i in range(1, len(s)):
            if helper(int(s[:i]), s[i:]):
                return True
        
        return False