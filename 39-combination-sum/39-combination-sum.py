class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        sol = set()
        
        def dfs(have, need):
            if need == 0:
                sol.add(tuple(sorted(have)))
                
            for i, c in enumerate(candidates):
                if c <= need:
                    dfs(have + [c], need - c)
        
        for i, c in enumerate(candidates):
            if c <= target:
                dfs([c], target - c)
                
        
        return sol