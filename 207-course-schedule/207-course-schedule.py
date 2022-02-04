class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = defaultdict(set)
        seen = set()

        for c, p in prerequisites:
            d[c].add(p)
        
        @cache
        def checkpath(c):
            seen.add(c)
            
            if c not in d:
                seen.remove(c)
                return True
            
            for p in d[c]:
                if p in seen or not checkpath(p):
                    return False

            seen.remove(c)
            return True
        
        return all(checkpath(c) for c in d)