class Solution:
    def minSteps(self, s: str, t: str) -> int:
        c_s, c_t = Counter(s), Counter(t)
        
        for c, count in c_t.items():
            if c in c_s:
                c_s[c] -= min(c_s[c], c_t[c])
      
        return sum(c_s.values())