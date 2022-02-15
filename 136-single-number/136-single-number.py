class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for k, v in Counter(nums).items():
            if v == 1:
                return k