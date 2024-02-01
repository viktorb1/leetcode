class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        sol = []
        for i in range(0, len(nums)-2, 3):
            if nums[i+1] - nums[i] <= k and nums[i+2] - nums[i+1] <= k and nums[i+2] - nums[i] <= k:
                sol.append(nums[i:i+3])
            else:
                return []
        
        return sol