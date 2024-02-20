class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        min_heap = []
        r, c = len(matrix), len(matrix[0])
        
        for i in range(min(k, r)):
            heappush(min_heap, (matrix[i][0], i, 0))
        
        for _ in range(k):
            ans, row, col = heappop(min_heap)
            if col + 1 < c: heappush(min_heap, (matrix[row][col+1], row, col+1))
        
        return ans