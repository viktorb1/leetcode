class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        self.min_range = float('inf')
        
        if k == len(cookies):
            return max(cookies)
        
        def dfs(x):
            if x == len(cookies): 
                print(data)
                self.min_range = min(max(data), self.min_range)
                return
            
            if max(data) >= self.min_range:
                return
            
            for j in range(k):
                data[j] += cookies[x]
                dfs(x+1)
                data[j] -= cookies[x]
                if data[j] == 0: break
        
        data = [0]*k
        dfs(0)
        return self.min_range