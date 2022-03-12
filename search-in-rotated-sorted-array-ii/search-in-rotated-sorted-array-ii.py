class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        
        while (low < high and nums[low] == nums[low+1]):
            low += 1
        while (low < high and nums[high] == nums[high-1]):
            high -= 1

        
        while low <= high:
            mid = (low + high) // 2
            
            if nums[mid] > nums[high] and target <= nums[high]:
                low = mid + 1
            elif nums[mid] < nums[low] and target >= nums[low]:
                high = mid
            else:
                if target < nums[mid]:
                    high = mid - 1
                elif target > nums[mid]:
                    low = mid + 1
                else:
                    return True
        
        return False