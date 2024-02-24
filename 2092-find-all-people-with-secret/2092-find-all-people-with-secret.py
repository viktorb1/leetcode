class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        graphs = defaultdict(dict)
        
        for x, y, t in meetings:
            if x not in graphs[t]:
                graphs[t][x] = set()
            if y not in graphs[t]:
                graphs[t][y] = set()
            
            graphs[t][x].add(y)
            graphs[t][y].add(x)
        
        know = {0, firstPerson}
        
        def flood(g, x, know):
            q = deque([x])
            
            while q:
                for i in range(len(q)):
                    n1 = q.popleft()
                    
                    for n2 in g[n1]:
                        if n2 not in know:
                            know.add(n2)
                            q.append(n2)
        
        seen_t = set()

        for x,y,t in sorted(meetings, key=lambda x: x[2]):
            if x in know and (x, t) not in seen_t:
                flood(graphs[t], x, know)
            
            if y in know and (y, t) not in seen_t:
                flood(graphs[t], y, know)
            
            seen_t.add((x,t))
            seen_t.add((y,t))
            
        
        
        return know