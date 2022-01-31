class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        memo = {}

        def mem(target):
            cs = 0
            
            if target == 0:
                return 1
            elif target in memo:
                return memo[target]

            for n in nums:
                if target - n >= 0:
                    cs += mem(target - n)
        
            memo[target] = cs
            return memo[target]
        
        return mem(target)