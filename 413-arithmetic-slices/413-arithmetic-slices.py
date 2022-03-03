class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        count = 0
        
        i = 0
        while i < len(nums)-1:
            start = i
            diff = nums[i+1] - nums[i]
            
            while i < len(nums)-1 and nums[i+1] - nums[i] == diff:
                i += 1
            
            length_of_longest_slice = i - start + 1
            
            for j in range(3, length_of_longest_slice + 1):
                count += length_of_longest_slice - j + 1
            
        return count