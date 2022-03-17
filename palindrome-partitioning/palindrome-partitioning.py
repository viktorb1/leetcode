class Solution:
    def partition(self, s: str) -> List[List[str]]:
        sols = []
        
        def dfs(s, sol):
            if not s:
                sols.append(sol)
            
            for i in range(1, len(s)+1):
                if s[:i] == s[:i][::-1]:
                    dfs(s[i:], sol + [s[:i]])
        
        dfs(s, [])
        return sols
                        
            