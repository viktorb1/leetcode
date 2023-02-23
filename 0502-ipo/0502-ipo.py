import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        opts = sorted(zip(profits, capital), key=lambda x: x[1])
        heap = []
        
        i = 0
        for _ in range(k):
            while i < len(opts) and opts[i][1] <= w:
                heapq.heappush(heap, -opts[i][0])
                i += 1

            if heap: w += -heapq.heappop(heap)
        
        return w