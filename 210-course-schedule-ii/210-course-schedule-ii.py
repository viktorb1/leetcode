class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        d = dict()
        
        for p in range(numCourses):
            d[p] = []
            
        for p1, p2 in prerequisites:
            d[p2].append(p1)

        def dfs(key):
            if key in visiting:
                return False
            elif key in visited:
                return True
            
            visiting.add(key)
            
            if key in d:
                for neighbor in d[key]:
                    if not dfs(neighbor):
                        return False
            
            visiting.discard(key)
            visited.add(key)
            sol.appendleft(key)
            return True
        
        sol = deque()
        visiting, visited = set(), set()
        
        for key in d.keys():
            if key not in visited:
                if not dfs(key):
                    return []
                
        return sol