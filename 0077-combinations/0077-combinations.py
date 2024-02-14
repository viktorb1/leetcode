class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        
        def dfs(i,c):
            nonlocal ans, n
            
            if len(c) == k:
                ans.append(c)
                return
            
            for i in range(i+1, n+1):
                dfs(i, c + [i])
        
        dfs(0, [])
        return ans