class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        max_heap = []
        
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                heappush(max_heap, -matrix[r][c])
                
                if len(max_heap) > k:
                    heappop(max_heap)
        
        return -heappop(max_heap)