class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        d = Counter(nums)
        keys = tuple(set(nums))
        nums.sort()
        
        @cache
        def dfs(keys):
            if not keys:
                return 0
            elif len(keys) == 1:
                return keys[0]*d[keys[0]]
            
            if keys[-2] != keys[-1] - 1:
                return keys[-1]*d[keys[-1]] + dfs(keys[:-1])
            else:
                return max(keys[-1]*d[keys[-1]] + dfs(keys[:-2]), dfs(keys[:-1]))
        
        return dfs(keys)
        