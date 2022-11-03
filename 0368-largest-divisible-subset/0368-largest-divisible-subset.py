class Solution:
    def largestDivisibleSubset(self, nums):
        
        @cache
        def dfs(i):
            if i == 0:
                return [nums[i]]
            
            largest = [nums[i]]
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    largest = max(dfs(j) + [nums[i]], largest, key=len)
            
            return largest
        
        nums.sort()
        largest = []
        for i in range(len(nums)-1, -1, -1):
            largest = max(dfs(i), largest, key=len)
        
        return largest
        