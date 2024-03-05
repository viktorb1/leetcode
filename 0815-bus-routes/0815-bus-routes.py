class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target: return 0
        routes = [set(r) for r in routes]
        seen_stops, seen_buses = set(), set()
        count = 0
        
        g = defaultdict(set)
        for i, r in enumerate(routes):
            for c in r:
                g[c].add(i)
        
        q = deque([source])
        while q:
            count += 1
            for _ in range(len(q)):
                bus_stop = q.popleft()
                seen_stops.add(bus_stop)
                
                for i in g[bus_stop]:
                    if i in seen_buses: continue
                    seen_buses.add(i)
                    for bus_stop_neighbor in routes[i]:
                        if bus_stop_neighbor == target:
                            return count
                        else:
                            if bus_stop_neighbor not in seen_stops:
                                q.append(bus_stop_neighbor)
            
        return -1