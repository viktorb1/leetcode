class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        """
        for i in range(len(nums)-1, 0, -1):
            if nums[i-1] < nums[i]:
                pivot = i-1
                swap = i
                while swap < len(nums)-1 and nums[swap+1] > nums[pivot]:
                    swap += 1

                nums[pivot], nums[swap] = nums[swap], nums[pivot] 
                nums[i:] = nums[i:][::-1] # reverse remainder
                return
        else:
            nums[:] = nums[::-1]
                