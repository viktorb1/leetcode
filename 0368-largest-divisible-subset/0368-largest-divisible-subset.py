class Solution:
    def largestDivisibleSubset(self, nums):
        nums.sort()
        sol = [[n] for n in nums]
        
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(sol[j]) + 1 > len(sol[i]):
                    sol[i] = sol[j] + [nums[i]]
        
        return max(sol, key=len)