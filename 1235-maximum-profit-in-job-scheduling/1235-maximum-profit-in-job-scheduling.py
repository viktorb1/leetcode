class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        n = len(startTime)
        jobs = sorted(zip(startTime, endTime, profit))
        startTimes = [i for i, _, _ in jobs]
        
        @lru_cache
        def dfs(i):
            if i == n:
                return 0
            
            ans = dfs(i+1)
            
            j = bisect_left(startTimes, jobs[i][1])
            ans = max(ans, dfs(j) + jobs[i][2])
            
            return ans
            
        return dfs(0)