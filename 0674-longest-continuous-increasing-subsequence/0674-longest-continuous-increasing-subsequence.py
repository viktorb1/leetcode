class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        length = 1
        largest_len = 1
        
        for n1, n2 in zip(nums, nums[1:]):
            if n2 > n1:
                length += 1
                largest_len = max(largest_len, length)
            else:
                length = 1
        
        return largest_len