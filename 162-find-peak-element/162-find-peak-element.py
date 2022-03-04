class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums = [float('-inf')] + nums + [float('-inf')]
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            mid = (start + end) // 2
            
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid-1
            elif nums[mid] < nums[mid-1]:
                end = mid - 1
            elif nums[mid] < nums[mid+1]:
                start = mid + 1
        
        return 0