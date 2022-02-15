class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter_t = Counter(t)
        need = set(t)
        l = 0
        coord = (float('-inf'), float('inf'))
        
        for r, c in enumerate(s):
            counter_t[c] -= 1
            
            if counter_t[c] == 0:
                need.discard(c)
                
            while len(need) == 0:
                coord = min(coord, (l, r), key = lambda x: x[1] - x[0])
                counter_t[s[l]] += 1
                
                if counter_t[s[l]] > 0:
                    need.add(s[l])
                
                l += 1
                    
        
        return s[coord[0]:coord[1]+1] if coord[0] != float('-inf') and coord[1] != float('inf') else ""
            