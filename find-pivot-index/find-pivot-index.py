class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            sum_left = sum(nums[0:i])
            sum_right = sum(nums[i+1:len(nums)])
            
            if sum_left == sum_right:
                return i
            
            
        return -1
                
        
        