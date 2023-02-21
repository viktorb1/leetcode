class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sol = set()
        
        for i, one in enumerate(nums[:-2]):
            l, r = i+1, len(nums)-1
            
            while l < r:
                total = one + nums[l] + nums[r]
                
                if total == 0:
                    sol.add((one, nums[l], nums[r]))
                    l += 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1
        
        return sol