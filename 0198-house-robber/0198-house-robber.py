class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0, 0] + [0]*len(nums)
            
        for j in range(2, len(dp)):
            dp[j] = max(nums[j-2] + dp[j-2], dp[j-1])
        
        return max(dp)