class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        q = [(0, 0), (0, firstPerson)]
        graph = defaultdict(list)
        
        for p1, p2, t in meetings:
            graph[p1].append((p2, t))
            graph[p2].append((p1, t))
        
        seen = set()
        while q:
            t, p1 = heappop(q)
            if p1 in seen:
                continue
            seen.add(p1)
            
            for p2, mt in graph[p1]:
                if mt >= t:
                    heappush(q, (mt, p2))
        
        return seen
        
        
        
        return know