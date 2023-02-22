class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, h = max(weights), sum(weights)
        
        while l < h:
            m = (l+h)//2
            
            if self.place_items(weights, m) > days:
                l = m+1
            else:
                h = m
        
        return l
            
    def place_items(self, weights, max_load):
        count = 1
        cur_weight = 0
        
        for w in weights:
            if cur_weight + w <= max_load:
                cur_weight += w
            else:
                count += 1
                cur_weight = w
        
        return count