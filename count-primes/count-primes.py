class Solution:
    def countPrimes(self, n: int) -> int:
        isPrime = [0, 0] + [1] * (n-2)
        count = 0
        
        for i in range(2, n):
            if not isPrime[i]:
                continue
            else:
                count += 1
                
                for j in range(i+i, n, i):
                    isPrime[j] = 0
                    
        return count