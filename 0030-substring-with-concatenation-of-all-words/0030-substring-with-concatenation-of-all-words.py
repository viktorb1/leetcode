class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(words[0])
        sol = []
        c1 = Counter(words)

        for offset in range(n):
            s_split = [s[i:i+n] for i in range(offset, len(s), n)]
            for i in range(len(s_split)-len(words)+1):
                c2 = Counter(s_split[i:i+len(words)])
                if c1 == c2: sol.append(i*n + offset)
        
        return sol
        