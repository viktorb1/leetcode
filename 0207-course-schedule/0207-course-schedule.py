class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = defaultdict(list)
        for c, p in prerequisites:
            g[c].append(p)
        
        @cache
        def ends_in_cycle(n):
            if n in seen: return True
            if n not in g: return False
            seen.add(n)
            for neighbor in g[n]:
                if neighbor not in seen:
                    if ends_in_cycle(neighbor):
                        return True
                else:
                    return True
            seen.remove(n)
            return False

        for node in g:
            seen = set()
            if ends_in_cycle(node):
                return False
        
        return True