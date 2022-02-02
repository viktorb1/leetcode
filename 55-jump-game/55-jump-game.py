class Solution:
    
    lru_cache(None)
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[-1] = True
        
        for i in range(len(nums)-2, -1, -1):
                dp[i] = any(dp[i:i+nums[i]+1])
            
        return dp[0]
        
        
#         def helper(i):
#             if i == len(nums) - 1:
#                 return True
            
#             ans = False
            
#             for j in range(i+1, min(i+nums[i]+1, len(nums))):
#                 ans |= helper(j)
            
#             return ans
            

#         return helper(0)
            