class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            if nums[mid] == target:
                return True
            elif nums[low] == nums[mid]:
                low += 1
            elif nums[low] <= target < nums[mid]:
                high = mid - 1
            elif nums[mid] < target <= nums[high]:
                low = mid + 1
            elif nums[low] <= nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
        
        return False