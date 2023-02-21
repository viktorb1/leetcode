class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums)-1
        
        while l <= h:
            m = (l+h)//2
            
            if nums[m] == target:
                return m
            elif nums[l] <= target < nums[m]:
                h = m-1
            elif nums[m] < target <= nums[h]:
                l = m+1
            elif nums[l] <= nums[m]:
                l = m+1
            else:
                h = m-1
            
        return -1