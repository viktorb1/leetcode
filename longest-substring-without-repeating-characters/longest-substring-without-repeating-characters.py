class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        max = 0
        count = 0
        
        for i in range(len(s)):
            for j in range(i, len(s)):
                if not s[j] in seen:
                    seen.add(s[j])
                    count += 1
                else:
                    if count > max:
                        max = count
                        
                    seen.clear()
                    count = 0
                    break
                    
            if count > max:
                max = count
                
        return max