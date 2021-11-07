class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        return [x for x in count if count[x] == 1]