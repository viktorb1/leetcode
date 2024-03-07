class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks = [-f for f in Counter(tasks).values()]
        heapify(tasks)
        bench = deque()
        time = 0

        while tasks or bench:
            time += 1

            if tasks:
                cur = heappop(tasks)
                cur += 1
                if cur < 0:
                    bench.append((cur, time + n))
            
            if bench and bench[0][1] == time:
                heappush(tasks, bench.popleft()[0])

        return time