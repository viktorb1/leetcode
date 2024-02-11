class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        memo = {}
        def dfs(r, c1, c2):
            nonlocal grid
            if r == len(grid): return 0
            if c1 == c2: return float('-inf')
            if (r, c1, c2) in memo: return memo[(r, c1, c2)]
            
            if 0 <= r < len(grid) and 0 <= c1 < len(grid[0]) and 0 <= c2 < len(grid[0]):
                max_pickup = 0
                
                for cl in [x for x in [c1-1, c1, c1+1] if 0 <= x < len(grid[0])]:
                    for cr in [x for x in [c2-1, c2, c2+1] if 0 <= x < len(grid[0])]:
                        ans = dfs(r+1, cl, cr)
                        max_pickup = max(max_pickup, ans)
                
                memo[(r, c1, c2)] = grid[r][c1] + grid[r][c2] + max_pickup
                return memo[(r, c1, c2)]
        
        return dfs(0, 0, len(grid[0])-1)