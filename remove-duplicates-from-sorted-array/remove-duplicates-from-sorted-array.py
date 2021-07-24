class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        next = 0
        
        for i in range(1, len(nums)):
            if nums[i] != nums[next]:
                next += 1
                nums[next] = nums[i]
                
        
        return next+1