class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        memo = {}
        
        def recur(i):
            if i < 0:
                return 0
            
            if i in memo:
                return memo[i]
            
            max_k = arr[i]
            max_val = float('-inf')
            for j in range(1, k+1):
                if i-j+1 >= 0:
                    max_k = max(max_k, arr[i-j+1])
                    max_val = max(max_val, max_k*j + recur(i-j))
            
            memo[i] = max_val
            return max_val
    
        return recur(len(arr)-1)
            