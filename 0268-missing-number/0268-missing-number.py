class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return ((len(nums) * (len(nums)+1)) // 2) - sum(nums)
        # if you're trying to sum the first nine numbers, do n(n+1)//2, with n=9