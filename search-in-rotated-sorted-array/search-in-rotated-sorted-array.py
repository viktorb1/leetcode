class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        mid = (low + high) // 2
        
        while low <= high:
            if target == nums[mid]:
                return mid
            elif nums[mid] > nums[high]:
                if target <= nums[mid] and target >= nums[low]:
                    high = mid - 1
                    mid = (low + high) // 2
                elif target >= nums[mid] or target <= nums[high]:
                    low = mid + 1
                    mid = (low + high) // 2
                else:
                    return -1
            elif nums[mid] < nums[high] and nums[mid] < nums[low]: # low case
                if target >= nums[mid] and target <= nums[high]:
                    low = mid + 1
                    mid = (low + high) // 2
                elif target <= nums[mid] or target >= nums[low]:
                    high = mid - 1
                    mid = (low + high) // 2
                else:
                    return -1
            elif nums[mid] <= nums[high] and nums[mid] >= nums[low]: # in order
                if target > nums[mid]:
                    low = mid + 1
                    mid = (low + high) // 2
                elif target < nums[mid]:
                    high = mid - 1
                    mid = (low + high) // 2
                else:
                    return -1
            else:
                return -1
            
        return -1
