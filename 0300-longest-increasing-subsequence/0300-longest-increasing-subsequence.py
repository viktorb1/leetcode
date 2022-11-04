class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for n in nums]
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(1 + dp[j], dp[i])
        
        return max(dp)