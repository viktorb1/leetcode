class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        c = Counter([b for _, b in trust])
        rest = {a for a, _ in trust}
        
        for k, v in c.items():
            if v == n-1 and k not in rest:
                return k
        
        return 1 if not len(trust) and n == 1 else -1