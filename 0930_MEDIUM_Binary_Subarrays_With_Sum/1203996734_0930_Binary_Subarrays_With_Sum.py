class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        c = Counter({0: 1})
        cum_sum = res = 0
        for i in nums:
            cum_sum += i
            res += c[cum_sum - goal]
            c[cum_sum] += 1
        return res