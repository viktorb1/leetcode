class Solution:
    @lru_cache(cache)
    def numDecodings(self, s: str) -> int:
        if not s:
            return 1

        total = 0

        if s[-1] != '0':
            total += self.numDecodings(s[:-1])
        
        if len(s) > 1 and s[-2] != '0' and int(s[-2:]) > 0 and int(s[-2:]) <= 26:
            total += self.numDecodings(s[:-2])
                
        return total
        
