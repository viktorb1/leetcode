class Solution:
    def countPrimes(self, n: int) -> int:
        prime = [0, 0] + [1] * (n-2)
        
        for i in range(2, n):
            if prime[i] == 1:
                prime[2*i:n:i] = [0] * len(prime[2*i:n:i])
        
        return sum(prime)