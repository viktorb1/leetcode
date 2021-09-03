class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 1
        
        while n >= 0:
            n -= i
            i += 1
        
        return i-2
    
    
# binary search solution
#
#
#     class Solution:
#     def arrangeCoins(self, n: int) -> int:
        
#         low = 1
#         high = n
#         mid  = (low + high) // 2
        
#         while low <= high:
#             lower = mid*(mid+1) // 2
#             upper = (mid+1)*(mid+2) // 2

#             if n >= lower and n <= upper:
#                 if n == upper:
#                     return mid + 1
#                 else:
#                     return mid
#             elif n < lower:
#                 high = mid - 1
#                 mid  = (low + high) // 2
#             elif n > upper:
#                 low = mid + 1
#                 mid  = (low + high) // 2
        
#         return -1
