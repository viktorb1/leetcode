class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, h = 0, len(nums) - 1
        
        if len(nums) == 1:
            return nums[0]
        elif nums[l] != nums[l+1]:
            return nums[l]
        elif nums[h] != nums[h-1]:
            return nums[h]
        
        while l <= h:
            m = (l + h) // 2
            
            if len({nums[m-1], nums[m], nums[m+1]}) == 3:
                return nums[m]
            elif m % 2 == 0:
                if nums[m] == nums[m+1]:
                    l = m + 1
                else:
                    h = m - 1
            elif m % 2 == 1:
                if nums[m] == nums[m+1]:
                    h = m - 1
                else:
                    l = m + 1