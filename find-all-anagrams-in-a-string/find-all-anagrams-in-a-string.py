class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        sol = []
        countp = Counter(p)
        counts = Counter(s[:len(p)])

        l = 0
        for r in range(len(p), len(s)):
            if countp == counts:
                sol.append(l)
            
            counts[s[r]] += 1
            counts[s[l]] -= 1
            l += 1
        
        if countp == counts:
            sol.append(l)
        
        return sol