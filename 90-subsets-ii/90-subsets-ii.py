class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        
        def dfs(i, sol):
            if i == len(nums):
                ans.add(tuple(sorted(sol)))
                return

            dfs(i+1, sol + [nums[i]])
            dfs(i+1, sol) 
    
        dfs(0, [])
        return ans