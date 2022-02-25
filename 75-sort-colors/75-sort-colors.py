class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors = {0: 0, 1: 0, 2: 0}
        
        for n in nums:
            colors[n] += 1
        
        i = 0
        for k, v in colors.items():
            for j in range(i, i+v):
                nums[j] = k
            i = i+v