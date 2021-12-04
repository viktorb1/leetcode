class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.choose([], sorted(nums), ans)
        return ans
    
    def choose(self, perm, nums, ans):
        if not nums:
            ans.append(perm)
        
        i = 0
        while i < len(nums):
            self.choose(perm + [nums[i]], nums[:i] + nums[i+1:], ans)
            
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
           
            i += 1
