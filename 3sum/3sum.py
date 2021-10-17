class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums.sort()
        
        for i in range(len(nums) - 2):
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            j = i + 1
            k = len(nums) - 1
            
            while j < k:
                curr_sum = nums[i] + nums[j] + nums[k]
                
                if curr_sum == 0:
                    ans.add((nums[i], nums[j], nums[k]))
                    j += 1
                elif curr_sum < 0:
                    j += 1
                else:
                    k -= 1

        return ans
