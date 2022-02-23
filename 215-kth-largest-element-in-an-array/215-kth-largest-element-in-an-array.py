import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(start, end, pivot):
            nums[pivot], nums[end] = nums[end], nums[pivot]
            
            divider = start
            for i in range(start, end):
                if nums[i] < nums[end]:
                    nums[divider], nums[i] = nums[i], nums[divider]
                    divider += 1
            
            nums[divider], nums[end] = nums[end], nums[divider]
            return divider
        
        def selectKth(start, end):
            if start == end:
                return nums[start]
            
            x = random.randint(start, end)
            divider = partition(start, end, x)

            if divider == len(nums) - k:
                return nums[divider]
            elif divider < len(nums) - k:
                return selectKth(divider+1, end)
            else:
                return selectKth(start, divider-1)
            
        return selectKth(0, len(nums)-1)
                    