class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c = Counter(nums)
        maxc = max(c.values())
        return sum([maxc for k, v in c.items() if v == maxc])