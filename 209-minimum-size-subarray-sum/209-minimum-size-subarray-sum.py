class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        smallest = float('inf')
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            
            while total >= target:
                smallest = min(smallest, i-l+1)
                total -= nums[l]
                l += 1
        
        return 0 if smallest == float('inf') else smallest
                