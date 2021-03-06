class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = defaultdict(set)
        seen = set()
        
        for c, p in prerequisites:
            d[c].add(p)
        
        @cache
        def dfs(e):            
            if e not in d:
                return True
                
            seen.add(e)
            
            for p in d[e]:
                if p in seen or not dfs(p):
                    return False
                
            seen.remove(e)
            return True
        
        
        for e in d:
            if not dfs(e):
                return False
        
        return True