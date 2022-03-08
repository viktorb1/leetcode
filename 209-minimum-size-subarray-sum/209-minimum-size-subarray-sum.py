class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minSize = float('inf')
        
        prefixsums = [0] + [0] * len(nums)
        for i in range(1, len(prefixsums)):
            prefixsums[i] = prefixsums[i-1] + nums[i-1]
            
        for i in range(len(nums)):
            low, high = i, len(nums) - 1
            
            while low <= high:
                mid = (low + high) // 2
                if prefixsums[mid+1] - prefixsums[i] >= target:
                    minSize = min(minSize, mid-i+1)
                    high = mid - 1
                else:
                    low = mid + 1
        
        return 0 if minSize == float('inf') else minSize