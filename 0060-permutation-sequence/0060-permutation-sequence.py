class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = tuple(str(i+1) for i in range(n))
        count = 0        
        
        
        def dfs(arr, ans=""):
            nonlocal count, nums
            if len(ans) == len(nums):
                if count == k-1:
                    return ans
                else:
                    count += 1
                    return

            for i, choose in enumerate(arr):
                result = dfs(arr[:i] + arr[i+1:], ans + choose)
                if result: return result
        
        return dfs(nums)