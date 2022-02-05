class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        options = set(nums)
        
        @lru_cache
        def dfs(n):
            if n not in options:
                return 0
            
            return 1 + dfs(n+1)
        
        max_count = 0
        for n in nums:
            if n-1 not in options:
                max_count = max(max_count, 1 + dfs(n+1))
            
        return max_count
            
                