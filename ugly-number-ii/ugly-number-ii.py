class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_nums = [1]
        i2, i3, i5 = 0, 0, 0
        
        while len(ugly_nums) < n:
            while ugly_nums[i2] * 2 <= ugly_nums[-1]: i2 += 1
            while ugly_nums[i3] * 3 <= ugly_nums[-1]: i3 += 1
            while ugly_nums[i5] * 5 <= ugly_nums[-1]: i5 += 1
            ugly_nums.append(min(ugly_nums[i2] * 2, ugly_nums[i3] * 3, ugly_nums[i5] * 5))
        
        return ugly_nums[-1]