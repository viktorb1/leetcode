class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ct = Counter(t)
        need = set(t)
        coord = (float('-inf'), float('inf'))
        
        l, r = 0, 0
        while r < len(s):
            ct[s[r]] -= 1
            if ct[s[r]] <= 0:
                need.discard(s[r])
            
            while len(need) == 0:
                coord = min((l, r + 1), coord, key = lambda x: x[1] - x[0])
                
                ct[s[l]] += 1
                if ct[s[l]] > 0:
                    need.add(s[l])
                l += 1
            r += 1

        return s[coord[0]:coord[1]] if coord[0] != float('-inf') and coord[1] != float('inf') else ""
        