class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        mask = 0xffffffff
        while b:
            sum = (a^b) & mask
            carry = ((a&b)<<1) & mask
            a = sum
            b = carry
            
        a &= mask
        if (a>>31) & 1:
            return ~(a^mask)
        
        return a