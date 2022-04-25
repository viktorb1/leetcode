class Solution:
    def primePalindrome(self, n: int) -> int:
        val = ''.join(['1'] + ['0'] * (len(str(n)) - 2) + ['1'])
        if n < 10: val = str(n)

        while not self.isPrime(int(val)) or int(val) < n:
            val = self.getNextPalindrome(val)
        
        return int(val)
        
    def getNextPalindrome(self, cur):
        cur = list(cur)
        int_val = int(''.join(cur[:(len(cur)+1)//2]))
        nex = list(str(int_val+1))
        
        if len(cur) % 2 == 1:
            if set(str(int_val)) == {'9'}:
                return ''.join(nex[:-1] + nex[::-1][1:])
            else:
                return ''.join(nex + nex[::-1][1:])
        else:
            if set(str(int_val)) == {'9'}:
                return ''.join(nex[:-1] + nex[::-1])
            else:
                return ''.join(nex + nex[::-1])
    
    
    def isPrime(self, n):
        if n == 1: return False
        for i in range(2, int(sqrt(n))+1):
            if n % i == 0:
                return False
        
        return True
        