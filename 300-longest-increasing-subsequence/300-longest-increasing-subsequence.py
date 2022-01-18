class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        def dfs(n, memo):
            ans = 1
            
            if memo[n] != -1:
                return memo[n]
            
            for i in range(n-1, -1, -1):
                if nums[i] < nums[n]:
                    rec_ans = 1 + dfs(i, memo)
                    ans = max(rec_ans, ans)

            memo[n] = ans
            return ans
        
        n = len(nums)
        ans = float('-inf')
        memo = [-1]*n
        for i in range(n-1, -1, -1):
            ans = max(dfs(i, memo), ans)
            
        return ans