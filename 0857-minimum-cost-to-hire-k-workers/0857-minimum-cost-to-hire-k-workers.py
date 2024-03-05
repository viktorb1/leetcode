class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        # someone will get paid their target wage, because if everyone got paid over their asking wage
        # then the solution is not optimal, since we can bring down everyone's salary little by little
        # until someone's salary hits their target salary
        
        # worker i's wage can be calculated from the captain's
        # worker i's wage =  (quality[i] / quality[captain]) * wage[captain]
        # let's call wage[captain] / quality[captain] the captain's ratio
        # using the ratio, we can calculate everyone else's expected wage and take the lowest k expected wages
        min_payment = float('inf')
        workers = sorted([(w/q, q, w) for q, w in zip(quality, wage)])
        wage_offer = []
        
        for i, (captain_ratio, q, w) in enumerate(workers):
            heappush(wage_offer, -q)
            # -q because we want to get rid of the highest paid worker remember quanity*captain_ratio = wage_offer
            
            if len(wage_offer) > k:
                heappop(wage_offer)
            
            if len(wage_offer) == k:
                min_payment = min(min_payment, -captain_ratio*sum(wage_offer))
        
        return min_payment