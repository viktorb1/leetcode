class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k_min = 1
        k_max = max(piles)
        
        while k_min < k_max:
            t = 0
            k = (k_min + k_max) // 2
            
            for p in piles:
                t += ceil(p/k)
            
            if t <= h:
                k_max = k
            else:
                k_min = k+1
                
        return k_max