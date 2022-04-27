import heapq

class Solution:
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        graph = DefaultDict(list)
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                d = abs(points[i][1] - points[j][1]) + abs(points[i][0] - points[j][0])
                graph[i].append((d, j))
                graph[j].append((d, i))
        
        heap = [n for n in graph[0]] # get all 0's neighbors
        heapq.heapify(heap)
        visited = {0}
        total = 0
        
        while heap and len(visited) < len(points):
            d, node = heapq.heappop(heap)
            if node not in visited:
                visited.add(node)
                total += d
                for di, ne in graph[node]:
                    if ne not in visited:
                        heapq.heappush(heap, (di, ne))
        
        return total