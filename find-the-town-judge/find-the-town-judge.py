class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        nums = set(range(1, n+1))
        trusts = dict()
        
        for v in range(1, n+1):
            trusts[v] = 0
        
        for t in trust:
            nums.discard(t[0])
            trusts[t[1]] += 1

        for t in trusts:
            if trusts[t] == n-1 and t in nums:
                return t
        
        return -1
        
            