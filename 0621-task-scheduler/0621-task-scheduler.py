class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        min_int = 0
        q = [(0, -v, k) for k, v in Counter(tasks).items()]
        heapify(q)
        cur_time = 0
        
        while q:
            c = max([(t, v, k) for t, v, k in q if t <= cur_time], key=lambda x: -x[1], default=None)
            
            if c:
                q.remove(c)
                heapify(q)
                t, v, k = c

                if v+1 < 0:
                    heappush(q, (cur_time + n + 1, v+1, k))
            
            cur_time += 1
        
        return cur_time