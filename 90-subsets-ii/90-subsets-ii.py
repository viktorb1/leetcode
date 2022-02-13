class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        
        def dfs(i, sol):
            if i == len(nums):
                ans.add(tuple(sorted(sol)))
                return

            for j in range(i, len(nums)):
                dfs(j+1, sol + [nums[j]])
                
            ans.add(tuple(sorted(sol)))
    
        dfs(0, [])
        return ans