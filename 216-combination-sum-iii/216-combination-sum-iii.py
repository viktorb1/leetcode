class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        choose = [i+1 for i in range(min(n, 9))]
        sol = []
        
        def dfs(choose, nums, total):
            if total == n and len(nums) == k:
                sol.append(nums)
                return

            for i, num in enumerate(choose):
                if total + num <= n and len(nums) < k:
                    dfs(choose[i+1:], nums + [num], total + num)
        
        dfs(choose, [], 0)
        return sol