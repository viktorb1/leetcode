class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        times = len(nums) // 3
        return [key for key, val in Counter(nums).items() if val > times]
        