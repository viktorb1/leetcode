class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        sol = set()
        
        def dfs(candidates, ans, cur_sum):
            if cur_sum == target:
                sol.add(tuple(sorted(ans)))
                return
                
            seen = set()
            for i, opt in enumerate(candidates):
                if opt in seen:
                    continue
                    
                seen.add(opt)
                if cur_sum + opt <= target:
                    dfs(candidates[i+1:], ans + [opt], cur_sum + opt)
        
        dfs(candidates, [], 0)
        return sol