class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        
        def robHelper(i):
            if i in memo:
                return memo[i]
            elif i < 0:
                return 0
            
            memo[i] = max(nums[i] + robHelper(i-2), robHelper(i-1))
            return memo[i] 
    
        return robHelper(len(nums)-1)