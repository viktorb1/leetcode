class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        
        if len(nums) == 1:
            return nums[0]
        elif nums[0] != nums[1]:
            return nums[0]
        elif nums[-1] != nums[-2]:
            return nums[-1]
        
        for i in range(1, len(nums), 3):
            if nums[i] != nums[i-1]:
                return nums[i-1]
        
        return -1