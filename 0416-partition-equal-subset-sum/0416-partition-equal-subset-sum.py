class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1: return False
        target = total // 2
        
        @cache
        def dfs(i, target):
            if target == 0:
                return True
            if target < 0 or i == len(nums):
                return False
            
            if dfs(i + 1, target - nums[i]):
                return True
            if dfs(i + 1, target):
                return True
        
        return dfs(0, target)