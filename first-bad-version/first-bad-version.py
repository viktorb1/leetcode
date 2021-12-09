# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        low = 1
        mid = n // 2
        high = n
        
        while low <= high:
            if isBadVersion(mid) and not isBadVersion(mid-1):
                return mid
            elif isBadVersion(mid):
                high = mid - 1
                mid = (low + high) // 2
            else:
                low = mid + 1
                mid = (low + high) // 2
                
