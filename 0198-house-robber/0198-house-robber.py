class Solution:
    def rob(self, nums: List[int]) -> int:
        
        @cache
        def robHelper(i):
            if i < 0:
                return 0
            
            return max(nums[i] + robHelper(i-2), robHelper(i-1))
    
        return robHelper(len(nums)-1)