class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        @cache
        def dfs(i):
            if manager[i] == -1:
                return 0
            
            return informTime[manager[i]] + dfs(manager[i])
        
        return max(dfs(i) for i in range(n))