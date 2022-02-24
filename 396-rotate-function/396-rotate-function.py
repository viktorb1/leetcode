class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        first = sum([i*j for i,j in zip(nums, range(len(nums)))])
        maxval = first
        sum_nums = sum(nums)
        
        for i in range(1, len(nums)):
            first = first + sum_nums - (nums[-i]*len(nums))
            maxval = max(maxval, first)
        
        return maxval
                