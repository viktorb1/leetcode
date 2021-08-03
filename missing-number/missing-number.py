class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        seen = {}
        
        for i in nums:
            seen[i] = 1
        
        for i in range(len(nums) + 1):
            if not i in seen:
                return i
