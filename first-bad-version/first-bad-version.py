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
            if isBadVersion(mid) == False:
                low = mid + 1
                mid = low + (high - low) // 2
            elif isBadVersion(mid) == True and isBadVersion(mid-1) == False:
                return mid
            else:
                high = mid - 1
                mid = low + (high - low) // 2
                    
        
                
                
                    
            