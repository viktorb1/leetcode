class Solution:
    def largestDivisibleSubset(self, nums):
        def dfs(i):
            if i in memo:
                return memo[i]
            elif i == 0:
                return [nums[i]]
            
            largest = [nums[i]]
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    largest = max(dfs(j) + [nums[i]], largest, key=len)
            
            memo[i] = largest
            return largest
        
        memo = {}
        nums.sort()
        largest = []
        for i in range(len(nums)-1, -1, -1):
            largest = max(dfs(i), largest, key=len)
        
        return largest
        