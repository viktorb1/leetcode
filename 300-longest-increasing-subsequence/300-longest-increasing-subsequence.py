class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        def dfs(n, memo):
            ans = 1
            
            if memo[n] != -1:
                return memo[n]
            
            for j in range(n-1, -1, -1):
                if nums[j] < nums[n]:
                    ans_rec = 1 + dfs(j, memo)
                    ans = max(ans, ans_rec)
            
            memo[n] = ans
            return ans
                    
        
        n = len(nums)
        ans = float('-inf')
        memo = [-1] * n
        
        for i in range(n-1, -1, -1):
            ans = max(ans, dfs(i, memo))
            
        return ans