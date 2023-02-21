class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        local_max, global_max = float('-inf'), float('-inf')
        for n in nums:
            local_max = max(local_max + n, n)
            global_max = max(local_max, global_max)
        return global_max