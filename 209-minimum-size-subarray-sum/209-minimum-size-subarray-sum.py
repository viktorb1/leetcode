class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        smallest = float('inf')
        
        prefixsums = [0] + [0] * len(nums)
        
        for i in range(1, len(prefixsums)):
            prefixsums[i] = prefixsums[i-1] + nums[i-1]
    
        for i in range(len(nums)):
            start, end = 0, len(prefixsums) - 1
            
            while start <= end:
                mid = (start + end) // 2
                if prefixsums[mid] - prefixsums[i] >= target:
                    smallest = min(smallest, mid-i)
                    end = mid - 1
                else:
                    start = mid + 1
            
        return smallest if smallest != float('inf') else 0