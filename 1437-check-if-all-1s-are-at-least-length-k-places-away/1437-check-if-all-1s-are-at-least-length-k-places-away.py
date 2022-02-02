class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        i = 0
        if k == 0:
            return True
        
        while i < len(nums):
            if nums[i] == 1:
                if sum(nums[i+1:i+k+1]) > 0:
                    return False
                i += k
            else:
                i += 1
        
        return True