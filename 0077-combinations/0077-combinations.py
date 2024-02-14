class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        
        def dfs(i,c):
            nonlocal ans, n
            
            if len(c) == k:
                ans.append(c)
            else:
                for j in range(i+1, n+1):
                    dfs(j, c + [j])
        
        dfs(0, [])
        return ans