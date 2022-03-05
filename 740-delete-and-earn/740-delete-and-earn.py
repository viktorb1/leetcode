class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        vals = sorted(set(nums))
        c = Counter(nums)
        sum1, sum2 = 0, 0
        
        for i, v in enumerate(vals):
            total = v*c[v]
            if vals[i-1] == vals[i] - 1:
                sum1, sum2 = sum2, max(total + sum1, sum2)
            else:
                sum1, sum2 = sum2, sum2 + total
        
        return sum2