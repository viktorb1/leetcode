class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        count = 0
        longest_slices = dict()
        
        i = 0
        while i < len(nums)-1:
            start = i
            diff = nums[i+1] - nums[i]
            
            while i < len(nums)-1 and nums[i+1] - nums[i] == diff:
                i += 1
            
            longest_slices[(start, i)] = i - start + 1
        
        for s in longest_slices:
            for i in range(3, longest_slices[s] + 1):
                count += longest_slices[s] - i + 1
        
        return count