class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = 0
        high = len(nums) - 1
        rang = [-1, -1]
        
        while low <= high:
            mid = (low + high) // 2

            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            elif nums[mid] == target:
                rang = [mid, mid]
                
                while rang[0] > 0 and nums[rang[0]-1] == nums[mid]:
                    rang[0] -= 1
                
                while rang[1] < len(nums) - 1 and nums[rang[1]+1] == nums[mid]:
                    rang[1] += 1
                    
                
                break

        return rang
