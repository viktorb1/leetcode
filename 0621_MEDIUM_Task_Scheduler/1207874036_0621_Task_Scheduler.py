class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks = sorted([-f for f in Counter(tasks).values()]) # how many times the task repeats
        bench = deque()
        time = 0

        while tasks or bench:
            time += 1

            if tasks:
                f = heappop(tasks)
                if f + 1 < 0:
                    bench.append((f + 1, time + n)) 
                    # we sit out the task until it becomes available again at time time+n 
            
            # remove all elements from bench that can be used again
            while bench and bench[0][1] == time: 
                heappush(tasks, bench.popleft()[0])

        return time