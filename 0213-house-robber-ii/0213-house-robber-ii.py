class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        memo = {}
        def rob_regular(arr, i):
            if i < 0:
                return 0
            elif i in memo:
                return memo[i]
            
            memo[i] = max(arr[i] + rob_regular(arr, i-2), rob_regular(arr, i-1))
            return memo[i]
        left = rob_regular(nums[:-1], len(nums)-2)
        memo.clear()
        right = rob_regular(nums[1:], len(nums)-2)
        return max(left, right)