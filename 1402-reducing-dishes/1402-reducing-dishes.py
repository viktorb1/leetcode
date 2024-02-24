class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        
        memo = {}
        def dfs(sat, c):
            if not sat:
                return 0
            
            if (len(sat), c) in memo:
                return memo[(len(sat), c)]
            
            maxval = dfs(sat[1:], c)
            maxval = max(maxval, sat[0]*c + dfs(sat[1:], c+1))
            memo[(len(sat), c)] = maxval
            return maxval
        
        return dfs(satisfaction, 1)