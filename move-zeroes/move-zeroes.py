class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lastZeroIndex = 0
        
        for i in nums:
            if i != 0:
                nums[lastZeroIndex] = i
                lastZeroIndex += 1
        
        for i in range(lastZeroIndex, len(nums)):
            nums[i] = 0
                
                
