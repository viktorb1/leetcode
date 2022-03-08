class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minSize = float('inf')
        
        prefixsums = [0] + [0] * len(nums)
        
        for i in range(1, len(prefixsums)):
            prefixsums[i] = prefixsums[i-1] + nums[i-1]
            
        print(prefixsums)
        for i in range(len(nums)):
            idx = bisect_left(prefixsums, target + prefixsums[i])
            if idx != len(prefixsums):
                minSize = min(minSize, idx-i)

        
        return 0 if minSize == float('inf') else minSize