class Solution:
    def nthSuperUglyNumber(self, n, primes):
        cand = [(p, p, 1) for p in primes]
        ugly = [1]
        
        while len(ugly) < n:
            ugly.append(cand[0][0])
            while cand[0][0] == ugly[-1]:
                _, p, i = heapq.heappop(cand)
                heapq.heappush(cand, (p*ugly[i], p, i+1))

        return ugly[-1]