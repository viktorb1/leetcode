class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(words[0])
        sol = []
        
        c1 = Counter(words)

        for offset in range(n):
            s_mod = [s[i:i+n] for i in range(offset, len(s), n)]

            i = 0
            while i+len(words) <= len(s_mod):
                c2 = Counter(s_mod[i:i+len(words)])
                if c1 == c2: sol.append(i*n + offset)
                i += 1
        
        return sol
        