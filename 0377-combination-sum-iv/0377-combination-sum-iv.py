class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}
        
        def dfs(target):
            if target in memo:
                return memo[target]
            if target < 0:
                return 0
            elif target == 0:
                return 1
            
            total = 0
            for n in nums:
                total += dfs(target-n)
            
            memo[target] = total
            return total
        
        return dfs(target)