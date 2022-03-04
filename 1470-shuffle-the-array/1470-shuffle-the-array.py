class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        i = 0
        j = len(nums) // 2
        ans = []
        
        while j < len(nums):
            if len(ans) % 2 == 0:
                ans.append(nums[i])
                i += 1
            else:
                ans.append(nums[j])
                j += 1    
        
        return ans