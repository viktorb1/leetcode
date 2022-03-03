class Solution:
    def jump(self, nums: List[int]) -> int:
        @cache
        def dfs(i):
            if i >= len(nums)-1:
                return 0

            ans=float('inf')
            for j in range(i, i + nums[i]):
                ans = min(ans,1 + dfs(j+1))
            return ans
        
        return dfs(0)