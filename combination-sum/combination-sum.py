class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def dfs(ans, candidates, target, sol):
            
            if target == 0 and sorted(sol) not in ans:
                ans.append(sorted(sol))
                return

            for c in candidates:
                if target >= c:
                    dfs(ans, candidates, target - c, sol + [c])
        
        ans = []
        dfs(ans, candidates, target, [])
        return ans