class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        mask = 0xffffffff
        # the purpose of the mask is to make negative numbers (and overflow) work
        
        while b:
            sum = (a^b) & mask
            # ^ is xor, which mimics addition
            carry = ((a&b)<<1) & mask
            # & is and, which calculates carries
            # << shifts the carries over one, since they needed to be added on the next number
            a = sum
            b = carry
            
        a = a & mask
        # anding with the mask (all 1's) makes a 32-bit long 
        
        if (a>>31) & 1: # checks if rightmost bit is a '1' which indicates a negative number
            return ~(a^mask)
            # a ^ mask flips the first 32 bits
            # ~ flips all bits (the point of all this is to make all numbers negative)
        
        return a
