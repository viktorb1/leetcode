class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        ans = None
        
        def countLessOrEqual(x):
            total = 0
            c = n - 1
            for r in range(m):
                while c >= 0 and matrix[r][c] > x: c -= 1
                total += (c+1)
            return total
    
        l, h = matrix[0][0], matrix[-1][-1]
        
        while l <= h:
            mid = (l+h) // 2
            
            if countLessOrEqual(mid) >= k:
                ans = mid
                h = mid - 1
            else:
                l = mid + 1
        
        return ans