
class Solution:
    def characterReplacement(self, s, k):
        counts = defaultdict(int)
        start = 0
        max_count = 0
        max_val = 0
        
        for end, c in enumerate(s):
            counts[c] += 1
            max_count = max(max_count, counts[c])
            
            if end - start + 1 - max_count > k:
                counts[s[start]] -= 1
                start += 1
            
            max_val = max(max_val, end - start + 1)
        
        return max_val
            
        