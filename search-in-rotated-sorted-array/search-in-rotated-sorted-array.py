class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            if target < nums[low] and nums[mid] >= nums[low]:
                low = mid + 1
            elif target > nums[high] and nums[mid] <= nums[high]:
                high = mid - 1
            else:                
                if target < nums[mid]:
                    high = mid - 1
                elif target > nums[mid]:
                    low = mid + 1
                else:
                    return mid
        
        return -1
