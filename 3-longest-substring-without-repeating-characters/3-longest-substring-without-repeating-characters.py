class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        start = 0
        max_len = 0
        
        for c in s:
            if c in seen:
                while s[start] != c:
                    seen.discard(s[start])
                    start += 1
                start += 1
            else:
                seen.add(c)
            
            max_len = max(len(seen), max_len)
        
        return max_len