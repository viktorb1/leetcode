import random

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        return self.shuffleHelper(self.nums)
        
    def shuffleHelper(self, nums):
        
        if not nums:
            return []
        
        pick = int(random.random() * len(nums))       
        return [nums[pick]] + self.shuffleHelper(nums[:pick] + nums[pick+1:])
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()