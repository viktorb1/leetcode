class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter_t = Counter(t)
        set_t = set(t)
        l = 0
        ans = s
        found_match = False
        
        for r, c in enumerate(s):
            counter_t[c] -= 1
            
            if counter_t[c] == 0:
                set_t.discard(c)
            
            while len(set_t) == 0:
                found_match = True
                ans = min(ans, s[l:r+1], key = lambda x: len(x))
                counter_t[s[l]] += 1
                
                if counter_t[s[l]] > 0:
                    set_t.add(s[l])
                
                l += 1
        
        return ans if found_match else ""