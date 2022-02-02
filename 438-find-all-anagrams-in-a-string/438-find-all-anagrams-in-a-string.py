class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        sol = []
        countp = Counter(p)
        counts = Counter(s[:len(p)-1])

        for i in range(len(s) - len(p) + 1):
            counts[s[i+len(p)-1]] += 1

            if countp == counts:
                sol.append(i)
                
            counts[s[i]] -= 1
                            
        return sol