class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            sum_left = sum(nums[0:i])
            sum_right = sum(nums[i+1:len(nums)])
            
            if sum_left == sum_right:
                return i
            
            
        return -1
    
    
    
# Alternative solution
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = sum(nums)
        
        for i in range(len(nums)):
            left_sum += nums[i]
            
            if left_sum == right_sum:
                return i
            
            right_sum -= nums[i]
            
        return -1
