class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        diff = 0
        maxlen = 0
        first_start = {0:0}
        
        for i, h in enumerate(hours, 1):
            diff += 1 if h > 8 else -1
            
            if diff > 0:
                maxlen = max(maxlen, i)
            if diff - 1 in first_start:
                maxlen = max(maxlen, i - first_start[diff-1])
            if diff not in first_start:
                first_start[diff] = i
                
        return maxlen