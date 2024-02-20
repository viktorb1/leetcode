class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        c = Counter(s)
        max_chars = len([i for i in c if c[i] >= k])
        ans = 0
        
        for uniq_limit in range(1, max_chars+1):
            chars_seen = defaultdict(int)
            num_uniq = 0
            start = 0
            for end in range(len(s)):
                chars_seen[s[end]] += 1
                
                if chars_seen[s[end]] == 1:
                    num_uniq += 1
                    
                while num_uniq > uniq_limit:
                    chars_seen[s[start]] -= 1
                
                    if chars_seen[s[start]] == 0:
                        num_uniq -= 1
                        del chars_seen[s[start]]
                    
                    start += 1
                
                if all(v >= k for v in chars_seen.values()):
                    ans = max(ans, end-start+1)
        
        return ans