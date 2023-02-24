class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(set)
        
        for c, p in prerequisites:
            adj[c].add(p)
        
        seen = set()
        
        @cache
        def check_ends(c):
            if c not in adj:
                return True
            
            seen.add(c)
            
            for p in adj[c]:
                if p in seen or not check_ends(p):
                    return False
            
            seen.remove(c)
            return True
        
        for c in adj:
            if not check_ends(c):
                return False
        
        return True