class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        total = 0
        
        for j, k in points:
            d = defaultdict(int)
            for l , m in points:
                dist = sqrt(pow(l-j, 2) + pow(m-k, 2))
                d[dist] += 1
            
            for k, v in d.items():
                if v > 1:
                    total += (v * (v-1))
        
        return total