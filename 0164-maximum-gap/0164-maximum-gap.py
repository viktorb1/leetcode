class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        max_gap = 0
        
        for n1, n2 in zip(nums, nums[1:]):
            max_gap = max(max_gap, n2-n1)
        
        return max_gap