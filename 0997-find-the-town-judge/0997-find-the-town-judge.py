class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        c = Counter([b for _, b in trust])
        rest = {a for a, _ in trust}
        if len(trust) == 0 and n == 1: return 1
        
        for k, v in c.items():
            if v == n-1 and k not in rest:
                return k
        
        return -1