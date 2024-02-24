class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:

        graph = defaultdict(list)
        for x, y, t in meetings:
            graph[x].append((t, y))
            graph[y].append((t, x))

        earliest = [inf] * n
        earliest[0] = 0
        earliest[firstPerson] = 0

        def dfs(person, time):
            for t, nextPerson in graph[person]:
                if t >= time and earliest[nextPerson] > t:
                    earliest[nextPerson] = t
                    dfs(nextPerson, t)

        dfs(0, 0)
        dfs(firstPerson, 0)
        
        return [i for i in range(n) if earliest[i] != inf]