class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        g = defaultdict(dict) # dict for representing graph
        for f, t, p in flights: g[f][t] = p
        
        heap = [(0, src, 0)] # heap to get minimum
        dist = [float('inf') for _ in range(n)]
        
        while heap:            
            w, u, count  = heappop(heap)
            
            if u == dst:
                return w
            
            if dist[u] < count:
                continue
            
            dist[u] = count
            

            if count <= k:
                for v, weight in g[u].items():
                    heappush(heap, (w + weight, v, count + 1))

        return -1 