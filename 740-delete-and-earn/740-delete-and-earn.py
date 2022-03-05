class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        vals = sorted(set(nums))
        c = Counter(nums)
        sum1, sum2 = 0, 0
        
        for i, v in enumerate(vals):
            if vals[i-1] == vals[i] - 1:
                sum1, sum2 = sum2, max(v*c[v] + sum1, sum2)
            else:
                sum1, sum2 = sum2, sum2 + v*c[v]
        
        return sum2