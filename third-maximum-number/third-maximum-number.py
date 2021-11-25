class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        dist = sorted(list(set(sorted(nums))))
        return dist[-3] if len(dist) > 2 else dist[-1]