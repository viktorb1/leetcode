class Solution:
    
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        x = Counter(s1)
        start, end = 0, len(s1)-1
        y = Counter(s2[start:end+1])
        
        while end <= len(s2):
            if x == y:
                return True
            elif end == len(s2) - 1:
                break
            
            y[s2[end+1]] += 1
            y[s2[start]] -= 1
            
            if y[s2[start]] == 0:
                del y[s2[start]]
            
            end += 1
            start += 1