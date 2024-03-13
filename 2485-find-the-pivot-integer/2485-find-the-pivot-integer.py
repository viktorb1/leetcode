class Solution:
    def pivotInteger(self, n: int) -> int:
        l, h = 0, n
        
        while l <= h:
            m = (l+h) // 2
            
            left = m * (m+1) // 2
            right = int((m + n) / 2 * (n-m+1))
            
            if left < right:
                l = m + 1
            elif left > right:
                h = m - 1
            else:
                return m
        
        return -1