class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        d = defaultdict(int)
        nums.sort()
        
        for n in nums:
            d[n] += n
         
        @cache
        def dfs(keys):
            if not keys:
                return 0
            elif len(keys) == 1:
                return d[keys[0]]
            
            if keys[-2] != keys[-1] - 1:
                return d[keys[-1]] + dfs(keys[:-1])
            else:
                return max(d[keys[-1]] + dfs(keys[:-2]), dfs(keys[:-1]))
        
        return dfs(tuple(d.keys()))
        