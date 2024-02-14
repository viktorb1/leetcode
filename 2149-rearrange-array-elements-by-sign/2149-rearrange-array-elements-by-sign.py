from queue import Queue

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p, n = 0, 0
        ans = [0] * len(nums)
        
        for i, a in enumerate(ans):
            if i % 2 == 0:
                while nums[p] < 0: p += 1
                ans[i] = nums[p]
                p += 1
            else:
                while nums[n] > 0: n += 1
                ans[i] = nums[n]
                n += 1
        
        return ans