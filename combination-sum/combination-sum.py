class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        self.dfs(ans, candidates, target, [])
        return ans
        
    
    def dfs(self, ans, candidates, target, sol):
        
        if target == 0 and sorted(sol) not in ans:
            ans.append(sorted(sol))
        elif target < 0:
            return
        else:
            for c in candidates:
                self.dfs(ans, candidates, target - c, sol + [c])
                
    
    
            
        