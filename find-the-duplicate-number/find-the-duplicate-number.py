class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i, n in enumerate(nums):
            if nums[abs(n)-1] < 0:
                return abs(n)
            else:
                nums[abs(n)-1] *= -1