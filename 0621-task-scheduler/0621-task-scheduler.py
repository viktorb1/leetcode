class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks = sorted([-f for f in Counter(tasks).values()]) # how many times the task repeats
        bench = deque()
        time = 0

        while tasks or bench:
            time += 1

            if tasks:
                cur = heappop(tasks)
                if cur + 1 < 0:
                    bench.append((cur + 1, time + n))
            
            if bench and bench[0][1] == time:
                heappush(tasks, bench.popleft()[0])

        return time