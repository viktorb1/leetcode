

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nmin, nmax = float('inf'), float('-inf')

        for n in nums:
            if n > 0:
                nmin = min(nmin, n)
                nmax = max(nmax, n)

        if nmin > 1: return 1
        rem = [0 for _ in range(len(nums))]

        for n in nums:
            if 0 < n <= len(nums):
                rem[n-1] = 1
        
        return rem.index(0)+1 if sum(rem) != len(nums) else nmax+1