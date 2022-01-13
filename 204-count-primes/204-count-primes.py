class Solution:
    def countPrimes(self, n: int) -> int:
        prime = [0, 0] + [1] * (n-2)
        count = 0
        
        for i in range(2, n):
            if prime[i]:
                count += 1
                
                for j in range(2*i, n, i):
                    prime[j] = 0
        
        return count