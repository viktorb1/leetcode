class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ct = Counter(t)
        need = set(t)
        minLen = float('inf')
        idxstart = 0
        
        l, r = 0, 0
        while r < len(s):
            if s[r] in ct:
                ct[s[r]] -= 1
                
                if ct[s[r]] == 0:
                    need.discard(s[r])
            
            while len(need) == 0:
                if r-l+1 < minLen:
                    minLen = r-l+1
                    idxstart = l
                
                if s[l] in ct:
                    ct[s[l]] += 1
                    if ct[s[l]] == 1:
                        need.add(s[l])
                  
                l += 1
            
            r += 1


        return s[idxstart:idxstart+minLen] if minLen != float('inf') else ""
                
            