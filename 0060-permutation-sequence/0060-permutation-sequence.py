class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [str(i+1) for i in range(n)]
        solutions = []
        
        
        def dfs(arr, ans=tuple()):
            nonlocal solutions
            if len(solutions) >= k:
                return
            if len(ans) == len(nums):
                solutions.append(ans)
                return

            
            for i, choose in enumerate(arr):
                dfs(arr[:i] + arr[i+1:], ans + (choose,))
        
        dfs(tuple(nums))
        return "".join(solutions[k-1])