class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        i = 1
            
        while i < n:
            i *= 2;
            
        return True if i == n else False
        

# Alternative solution
# Example 15 = 01111 and 16 = 10000
# class Solution:
#     def isPowerOfTwo(self, n: int) -> bool:
#         return n > 0 and (n & (n - 1) == 0)
