class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        n = len(nums)
        dp = [-1]*n
        
        for i in range(0, n):
            dp[i] = 1
            
            for j in range(0, i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])
        
        return max(dp)