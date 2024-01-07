class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        counts = [defaultdict(int) for _ in nums]
        ans = 0
        
        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                ans += counts[j][diff]
                counts[i][diff] += (counts[j][diff] + 1)
        
        return ans