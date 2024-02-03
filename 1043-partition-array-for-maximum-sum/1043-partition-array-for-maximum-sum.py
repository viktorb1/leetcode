class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [0] * k + arr
        
        for i in range(k, len(dp)):
            max_k = dp[i]
            max_val = float('-inf')
            for j in range(1, k+1):
                if i-k-j+1 >= 0:
                    max_k = max(max_k, arr[i-k-j+1])
                    dp[i] = max(dp[i], max_k*j + dp[i-j])
            
        return dp[-1]