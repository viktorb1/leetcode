class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = defaultdict(set)

        for c, p in prerequisites:
            d[c].add(p)

        status = [0] * numCourses
                   
        def checkpath(c):
            status[c] = -1

            if c not in d:
                status[c] = 1
                return True

            for p in d[c]:
                if status[p] == 1:
                    continue

                if status[p] == -1 or not checkpath(p):
                    return False
            
            status[c] = 1
            return True
        
        for c in d:
            if not checkpath(c):
                return False
       
        return True
