class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        removed = 0
        i = 0
        while i < len(nums)-removed-2:
            if nums[i] == nums[i+1] == nums[i+2]:
                for j in range(i+2, len(nums)-removed-1):
                    nums[j] = nums[j+1]
                
                removed += 1
            else:
                i += 1
        
        return len(nums) - removed