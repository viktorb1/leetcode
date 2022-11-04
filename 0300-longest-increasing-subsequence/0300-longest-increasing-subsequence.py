class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        @cache
        def lis(i):
            if i == -1:
                return 0
            
            largest = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    largest = max(1 + lis(j), largest)
        
            return largest
        
        largest = 0
        for i in range(len(nums)-1, -1, -1):
            largest = max(lis(i), largest)
        
        return largest