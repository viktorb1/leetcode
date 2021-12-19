class Solution:

    def rob(self, nums: List[int]) -> int:
        subprob = [-1] * len(nums)
        return self.get(nums, subprob, 0)
            
    def get(self, nums, subprob, i):
        if i >= len(nums):
            return 0
        elif subprob[i] >= 0:
            return subprob[i]
        
        subprob[i] =  max(nums[i] + self.get(nums, subprob, i+2), self.get(nums, subprob, i+1))
        return subprob[i]
        